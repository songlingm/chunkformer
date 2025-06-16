#!/bin/bash

echo "🔍 Đang kiểm tra các dịch vụ Bluetooth Auto-Pairing đã cài..."

SERVICES=(
"bluetooth-agent.service"
"bluetooth-startup.service"
"bluetooth-autopair.service"
"bluetooth-autoscan.service"
"bluetooth-auto-pairing.service"
)

for SERVICE in "${SERVICES[@]}"; do
    if systemctl list-units --full -all | grep -Fq "$SERVICE"; then
        echo "✅ Đã phát hiện service: $SERVICE"
        systemctl status $SERVICE --no-pager | grep "Active:"
    else
        echo "❌ Không tìm thấy service: $SERVICE"
    fi
done

echo "🔎 Quét hoàn tất!"
