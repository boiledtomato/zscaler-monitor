#!/bin/bash
# Zscaler監視スクリプト起動ラッパー
cd "$(dirname "$0")"
python3 zscaler_monitor.py >> logs/monitor.log 2>&1
