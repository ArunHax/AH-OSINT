<div align="center">

# 🔍 AH-OSINT

### Passive Open Source Intelligence (OSINT) Framework

A modular Python-based OSINT framework for gathering publicly available intelligence on domains, IP addresses, DNS records, and websites.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Version](https://img.shields.io/badge/Version-v0.1.0-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

Developed by **ArunHax**

</div>

---

# 📖 Overview

AH-OSINT is a lightweight, modular, passive OSINT framework designed for security researchers, students, bug bounty hunters, and defenders.

It performs passive intelligence gathering against publicly available sources without attempting exploitation or intrusive scanning.

The project is designed with simplicity, readability, and extensibility in mind, making it suitable for both learning and practical reconnaissance.

---

# ✨ Features

## 🌐 Domain Intelligence

- Domain WHOIS lookup
- Registrar information
- Creation & expiration dates
- Name servers
- Domain status
- WHOIS parsing

---

## 🌍 IP Intelligence

- IPv4 / IPv6 detection
- Private/Public IP detection
- Country
- Region
- City
- ZIP Code
- Latitude & Longitude
- Timezone
- ISP
- Organization
- ASN
- Reverse DNS lookup
- Google Maps location

---

## 📡 DNS Intelligence

Supports lookup of:

- A
- AAAA
- MX
- NS
- TXT
- CNAME
- SOA

---

## 🖥 Website Intelligence

- HTTP Status Code
- HTTPS detection
- Redirect detection
- Response time
- Server headers
- Security headers
- robots.txt check
- sitemap.xml check
- Host IP resolution

---

## 📄 Report Generation

Every completed scan is automatically saved as a structured JSON report.

Example:

```
outputs/ip_157.51.xxx.xxx_20260728_183000.json
```

---

# 📂 Project Structure

```text
AH-OSINT/
│
├── modules/
│   ├── domain.py
│   ├── ip.py
│   ├── dns_osint.py
│   └── website.py
│
├── outputs/
│
├── screenshots/
│
├── utils/
│   ├── helpers.py
│   └── output.py
│
├── config.py
├── ah-osint.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ArunHax/AH-OSINT.git
```

Go into the project

```bash
cd AH-OSINT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run AH-OSINT

```bash
python ah-osint.py
```

---

# 🚀 Usage

Launch the framework:

```bash
python ah-osint.py
```

Example:

```text
AH-OSINT Framework v0.1.0

01  Domain Intelligence
02  IP Intelligence
03  DNS Intelligence
04  Website Intelligence
05  Exit

Select >
```

---

# 📸 Screenshots

## Main Menu

> Add screenshot here

```
screenshots/main-menu.png
```

---

## IP Intelligence

> Add screenshot here

```
screenshots/ip-intelligence.png
```

---

## DNS Intelligence

> Add screenshot here

```
screenshots/dns-intelligence.png
```

---

## Website Intelligence

> Add screenshot here

```
screenshots/website-intelligence.png
```

---

# 📦 Output Reports

AH-OSINT automatically stores every completed scan inside the **outputs/** directory.

Example:

```text
outputs/
├── dns_google.com_20260728_182400.json
├── ip_157.51.xxx.xxx_20260728_183000.json
└── website_example.com_20260728_183500.json
```

---

# 🛣 Roadmap

## v0.1.0 ✅

- Domain Intelligence
- IP Intelligence
- DNS Intelligence
- Website Intelligence
- JSON Report Export
- Rich Terminal Interface

---

## Planned Features

- SSL/TLS Certificate Analysis
- Security Header Scoring
- Website Technology Detection
- CDN Detection
- WAF Detection
- Email Intelligence
- HTML Report Export
- CSV Export
- Plugin System
- Concurrent Scanning
- Additional OSINT Modules

---

# 🛡 Disclaimer

AH-OSINT is intended solely for:

- Educational purposes
- Defensive security research
- Authorized penetration testing
- Security awareness

Always obtain proper authorization before performing reconnaissance or security testing against systems you do not own or manage.

The author is not responsible for any misuse of this project.

---

# 🤝 Contributing

Contributions, feature requests, bug reports, and suggestions are welcome.

If you discover a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

# 📜 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**ArunHax**

Cybersecurity • OSINT • Ethical Hacking

GitHub:
https://github.com/ArunHax

---

<div align="center">

### ⭐ If you find AH-OSINT useful, consider giving this repository a star!

Made by ArunHax

</div>
