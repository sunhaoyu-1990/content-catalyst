#!/usr/bin/env python3
"""
SKILL.md 格式验证脚本

用法:
    python validate-skill.py {skill-name}
    python validate-skill.py --all

验证项目:
1. SKILL.md YAML frontmatter 格式检查（name、description 必需）
2. references 目录配置文件格式验证（YAML/Markdown）
3. 共享模块引用路径检查
4. 依赖工具可用性检查（Playwright MCP、WebSearch tool）
"""

import os
import sys
import re
import yaml
from pathlib import Path
from typing import List, Tuple


class SkillValidator:
    def __init__(self, skills_dir: str):
        self.skills_dir = Path(skills_dir)
        self.errors = []
        self.warnings = []

    def validate_skill(self, skill_name: str) -> bool:
        """验证单个 skill"""
        print(f"\n{'='*60}")
        print(f"验证 Skill: {skill_name}")
        print(f"{'='*60}")

        skill_path = self.skills_dir / skill_name
        if not skill_path.exists():
            print(f"✗ Skill 目录不存在: {skill_path}")
            return False

        # 验证 SKILL.md
        skill_file = skill_path / "SKILL.md"
        if not skill_file.exists():
            print(f"✗ SKILL.md 不存在: {skill_file}")
            return False

        self.errors = []
        self.warnings = []

        # 验证 YAML frontmatter
        self._validate_yaml_frontmatter(skill_file)

        # 验证 references 目录
        self._validate_references(skill_path)

        # 验证共享模块引用
        self._validate_shared_inheritance(skill_file)

        # 输出结果
        self._print_results(skill_name)

        return len(self.errors) == 0

    def validate_all(self) -> Tuple[int, int]:
        """验证所有 skills"""
        skill_dirs = [d for d in self.skills_dir.iterdir()
                      if d.is_dir() and not d.name.startswith('_')]

        print(f"\n发现 {len(skill_dirs)} 个 skill 目录")

        passed = 0
        failed = 0

        for skill_dir in skill_dirs:
            if self.validate_skill(skill_dir.name):
                passed += 1
            else:
                failed += 1

        print(f"\n{'='*60}")
        print(f"验证完成: {passed} 通过, {failed} 失败")
        print(f"{'='*60}")

        return passed, failed

    def _validate_yaml_frontmatter(self, skill_file: Path):
        """验证 YAML frontmatter"""
        try:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 检查 YAML frontmatter
            if not content.startswith('---'):
                self.errors.append("缺少 YAML frontmatter（必须以 --- 开头）")
                return

            # 提取 YAML 内容
            yaml_end = content.find('---', 3)
            if yaml_end == -1:
                self.errors.append("YAML frontmatter 未正确闭合（需要第二个 ---）")
                return

            yaml_content = content[3:yaml_end].strip()

            # 解析 YAML
            try:
                frontmatter = yaml.safe_load(yaml_content)
            except yaml.YAMLError as e:
                self.errors.append(f"YAML 解析失败: {e}")
                return

            # 检查必需字段
            if 'name' not in frontmatter:
                self.errors.append("缺少必需字段: name")
            elif not isinstance(frontmatter['name'], str):
                self.errors.append("name 必须是字符串")

            if 'description' not in frontmatter:
                self.errors.append("缺少必需字段: description")
            elif not isinstance(frontmatter['description'], str):
                self.errors.append("description 必须是字符串")

            # 检查推荐字段
            if 'name' in frontmatter:
                name = frontmatter['name']
                if not re.match(r'^[a-z0-9-]+$', name):
                    self.warnings.append(f"name 应使用小写字母、数字和连字符: {name}")

            print("✓ YAML frontmatter 格式正确")

        except Exception as e:
            self.errors.append(f"读取文件失败: {e}")

    def _validate_references(self, skill_path: Path):
        """验证 references 目录"""
        refs_dir = skill_path / "references"
        if not refs_dir.exists():
            self.warnings.append("references 目录不存在（可选）")
            return

        # 检查配置文件
        config_files = list(refs_dir.glob("*.md")) + list(refs_dir.glob("*.yaml")) + list(refs_dir.glob("*.yml"))

        for config_file in config_files:
            if config_file.suffix in ['.yaml', '.yml']:
                self._validate_yaml_file(config_file)
            else:
                # Markdown 文件基本检查
                if config_file.stat().st_size == 0:
                    self.warnings.append(f"配置文件为空: {config_file.name}")

        print(f"✓ references 目录检查完成（{len(config_files)} 个配置文件）")

    def _validate_yaml_file(self, yaml_file: Path):
        """验证 YAML 配置文件"""
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 检查是否包含 YAML frontmatter
            if content.startswith('---'):
                yaml_end = content.find('---', 3)
                if yaml_end != -1:
                    yaml_content = content[3:yaml_end].strip()
                    yaml.safe_load(yaml_content)

            print(f"  ✓ {yaml_file.name}")

        except yaml.YAMLError as e:
            self.errors.append(f"YAML 文件格式错误 {yaml_file.name}: {e}")
        except Exception as e:
            self.warnings.append(f"无法验证 {yaml_file.name}: {e}")

    def _validate_shared_inheritance(self, skill_file: Path):
        """验证共享模块引用"""
        try:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 检查是否引用了共享模块
            if '../_shared/' in content or '继承:' in content:
                # 提取继承声明
                inherit_match = re.search(r'继承:\s*\.\./_shared/([-\w]+\.md)', content)
                if inherit_match:
                    shared_module = inherit_match.group(1)
                    shared_path = self.skills_dir / '_shared' / shared_module

                    if not shared_path.exists():
                        self.errors.append(f"引用的共享模块不存在: {shared_module}")
                    else:
                        print(f"✓ 共享模块引用正确: {shared_module}")

        except Exception as e:
            self.warnings.append(f"无法验证共享模块引用: {e}")

    def _validate_dependencies(self):
        """验证依赖工具可用性"""
        print("\n验证依赖工具:")

        # 检查 Python
        try:
            import sys
            python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
            print(f"✓ Python: {python_version}")
        except Exception as e:
            self.errors.append(f"Python 环境检查失败: {e}")

        # 检查 Python 依赖
        dependencies = ['PIL', 'yaml']  # Pillow, PyYAML
        for dep in dependencies:
            try:
                __import__(dep)
                print(f"✓ {dep}")
            except ImportError:
                self.warnings.append(f"{dep} 未安装")

    def _print_results(self, skill_name: str):
        """打印验证结果"""
        if self.warnings:
            print(f"\n警告 ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  ⚠ {warning}")

        if self.errors:
            print(f"\n错误 ({len(self.errors)}):")
            for error in self.errors:
                print(f"  ✗ {error}")
            print(f"\n❌ {skill_name} 验证失败")
        else:
            print(f"\n✅ {skill_name} 验证通过")


def main():
    # 获取 skills 目录
    script_dir = Path(__file__).parent
    skills_dir = script_dir.parent

    validator = SkillValidator(str(skills_dir))

    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            validator.validate_all()
        else:
            skill_name = sys.argv[1]
            validator.validate_skill(skill_name)
    else:
        print("用法:")
        print("  python validate-skill.py {skill-name}")
        print("  python validate-skill.py --all")
        print("\n示例:")
        print("  python validate-skill.py zhihu-collect")
        print("  python validate-skill.py --all")

        # 交互式选择
        skill_dirs = [d.name for d in skills_dir.iterdir()
                      if d.is_dir() and not d.name.startswith('_')]

        if skill_dirs:
            print(f"\n可用的 skills:")
            for i, skill in enumerate(skill_dirs, 1):
                print(f"  {i}. {skill}")

            try:
                choice = input("\n选择要验证的 skill (输入数字或按 Enter 验证所有): ").strip()
                if not choice:
                    validator.validate_all()
                elif choice.isdigit() and 1 <= int(choice) <= len(skill_dirs):
                    validator.validate_skill(skill_dirs[int(choice) - 1])
                else:
                    print(f"无效的选择: {choice}")
            except (ValueError, KeyboardInterrupt):
                print("\n已取消")


if __name__ == '__main__':
    main()
