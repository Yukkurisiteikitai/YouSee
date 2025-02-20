#!/usr/bin/env python3
import subprocess
import sys
import os

def check_changes():
    """
    git status --porcelain で変更（追加・修正・未追跡）があるかを確認する。
    出力があれば True、なければ False を返す。
    """
    result = subprocess.run(["git", "status", "--porcelain"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    return bool(result.stdout.strip())

def git_add():
    """すべての変更をステージする"""
    result = subprocess.run(["git", "add", "."],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    if result.returncode != 0:
        print("git add に失敗しました:", result.stderr)
        sys.exit(1)

def git_commit():
    """コミットメッセージ「定期実行」でコミットする"""
    result = subprocess.run(["git", "commit", "-m", "Regular execution(record)"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    if result.returncode != 0:
        print("git commit に失敗しました:", result.stderr)
        sys.exit(1)

def git_push():
    """変更をリモートに push する"""
    result = subprocess.run(["git", "push"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    if result.returncode != 0:
        print("git push に失敗しました:", result.stderr)
        sys.exit(1)

def main():
    # スクリプトを実行するディレクトリが Git リポジトリか確認
    if not os.path.exists(".git"):
        print("このディレクトリは git リポジトリではありません。")
        sys.exit(1)

    # 変更がなければ終了
    if not check_changes():
        print("変更は検知されませんでした。")
        return 0

    # 変更があればステージ→コミット→push を実行
    git_add()
    git_commit()
    git_push()
    print("変更をコミットして push しました。")
    return 1

if __name__ == "__main__":
    main()
