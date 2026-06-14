#!/bin/bash
grep -E '^smtpd_tls_security_level|^smtpd_use_tls|^smtp_tls_security_level|^smtpd_tls_mandatory_protocols|^smtpd_tls_mandatory_ciphers' /etc/postfix/main.cf 2>/dev/null | grep -v '^#' || echo "STARTTLS not configured"
