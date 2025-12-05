import re
import os
from datetime import datetime


log_file_path = "server_logs.txt"

sample_logs = """
2025-12-05 10:00:01 [INFO] User admin logged in successfully.
2025-12-05 10:05:23 [ERROR] Failed login attempt for user root from 192.168.1.50
2025-12-05 10:05:25 [ERROR] Failed login attempt for user root from 192.168.1.50
2025-12-05 10:05:27 [ERROR] Failed login attempt for user root from 192.168.1.50
2025-12-05 10:15:00 [INFO] User kaan visited /home
2025-12-05 10:20:00 [WARNING] Suspicious query detected: SELECT * FROM users WHERE '1'='1'
2025-12-05 10:22:10 [INFO] Connection closed.
"""


with open(log_file_path, "w") as f:
    f.write(sample_logs)

print(f"[*] Örnek log dosyası oluşturuldu: {log_file_path}")


def analyze_logs(file_path):
    print(f"[*] Log analizi başlatılıyor: {datetime.now()}")
    print("-" * 50)
    
    suspicious_patterns = {
        "Brute Force Attempt": r"Failed login attempt",
        "SQL Injection Attempt": r"SELECT .* FROM",
        "Suspicious Activity": r"UNION SELECT"
    }
    
    issues_found = 0
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                for attack_type, pattern in suspicious_patterns.items():
                    if re.search(pattern, line, re.IGNORECASE):
                        print(f"[!] TEHDİT TESPİT EDİLDİ: {attack_type}")
                        print(f"    Log: {line.strip()}")
                        issues_found += 1
    except FileNotFoundError:
        print("[-] Hata: Log dosyası bulunamadı.")
        return

    print("-" * 50)
    if issues_found > 0:
        print(f"[+] Analiz tamamlandı. Toplam {issues_found} şüpheli işlem bulundu.")
    else:
        print("[+] Sistem temiz. Şüpheli işlem bulunamadı.")


if __name__ == "__main__":
    analyze_logs(log_file_path)