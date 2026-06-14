
## 1. IP Ranges

All hosts are hosted on AWS EC2 in eu-west-3 (Paris, France):

| IP Address | Subdomain | AWS Hostname |
|------------|-----------|--------------|
| 35.181.10.155 | read.holbertonschool.com | ec2-35-181-10-155.eu-west-3.compute.amazonaws.com |
| 35.181.141.244 | read.holbertonschool.com | ec2-35-181-141-244.eu-west-3.compute.amazonaws.com |
| 15.188.95.246 | apply.holbertonschool.com | ec2-15-188-95-246.eu-west-3.compute.amazonaws.com |
| 51.44.28.84 | apply.holbertonschool.com | ec2-51-44-28-84.eu-west-3.compute.amazonaws.com |
| 35.180.145.93 | apply.holbertonschool.com | ec2-35-180-145-93.eu-west-3.compute.amazonaws.com |
| 35.181.209.82 | apply.holbertonschool.com | ec2-35-181-209-82.eu-west-3.compute.amazonaws.com |
| 13.37.205.47 | apply.holbertonschool.com | ec2-13-37-205-47.eu-west-3.compute.amazonaws.com |
| 51.45.18.159 | apply.holbertonschool.com | ec2-51-45-18-159.eu-west-3.compute.amazonaws.com |
| 52.47.143.83 | yriry2.holbertonschool.com | ec2-52-47-143-83.eu-west-3.compute.amazonaws.com |

### Inferred CIDR Ranges:
- 35.180.0.0/16
- 35.181.0.0/16
- 15.188.0.0/16
- 13.37.0.0/16
- 51.44.0.0/16
- 51.45.0.0/16
- 52.47.0.0/16

## 2. Subdomains Discovered

| Subdomain | Purpose |
|-----------|---------|
| apply.holbertonschool.com | Admission portal |
| read.holbertonschool.com | Reading portal (authenticated) |
| yriry2.holbertonschool.com | Level2 Forum |

## 3. Technologies & Frameworks

### Web Servers
| Subdomain | Server | Version |
|-----------|--------|---------|
| apply.holbertonschool.com | nginx | 1.20.0 |
| read.holbertonschool.com | nginx | 1.20.0 |
| yriry2.holbertonschool.com | nginx | (undisclosed) |

### SSL/TLS Certificates
| Subdomain | Issued By | Organization | TLS Versions |
|-----------|-----------|--------------|--------------|
| apply.holbertonschool.com | Amazon RSA 2048 M02 | Amazon | TLSv1.2 |
| read.holbertonschool.com | Amazon RSA 2048 M04 | Amazon | TLSv1.2 |
| yriry2.holbertonschool.com | YE1 (Let's Encrypt) | Let's Encrypt | TLSv1.2, TLSv1.3 |

### Cloud Infrastructure
| Component | Details |
|-----------|---------|
| Provider | Amazon Web Services (AWS) |
| Service | EC2 |
| Region | eu-west-3 (Paris, France) |
| ISP | Amazon Data Services France, A100 ROW Inc |

### Security Headers (Present on all subdomains)
| Header | Value |
|--------|-------|
| X-Frame-Options | SAMEORIGIN |
| X-Content-Type-Options | nosniff |
| X-Download-Options | noopen |
| X-XSS-Protection | 1; mode=block (0 on yriry2) |

## 4. HTTP Response Analysis

| Subdomain | Status Code | Title |
|-----------|-------------|-------|
| apply.holbertonschool.com | 200 OK | "Welcome to Holberton School admission portal" |
| read.holbertonschool.com | 401 Unauthorized | (Authentication required) |
| yriry2.holbertonschool.com | 200 OK | "Holberton School Level2 Forum" |

## 5. Summary

| Category | Findings |
|----------|----------|
| Total IPs Found | 9 |
| Unique Subdomains | 3 |
| Web Server | nginx |
| Cloud Provider | AWS (Paris) |
| Certificate Authority | Amazon & Let's Encrypt |
| Security Headers | 4 implemented |

## 6. Commands Reference

Used :

```bash
# Shodan CLI commands (if API key configured)
shodan search hostname:"holbertonschool.com"
shodan search ssl:"holbertonschool.com"
shodan domain holbertonschool.com

# Web interface searches
# https://www.shodan.io/search?query=hostname%3A%22holbertonschool.com%22
# https://www.shodan.io/search?query=ssl%3A%22holbertonschool.com%22
