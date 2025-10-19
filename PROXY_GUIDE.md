# Proxy Rotation Guide

## Table of Contents
- [Why Proxies Matter](#why-proxies-matter)
- [How Proxy Rotation Works](#how-proxy-rotation-works)
- [Setting Up Proxies](#setting-up-proxies)
- [Proxy Formats](#proxy-formats)
- [Finding Proxy Providers](#finding-proxy-providers)
- [Testing Proxies](#testing-proxies)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## Why Proxies Matter

### Without Proxies
When you run the bot without proxies:
- ❌ All sessions use YOUR IP address
- ❌ Platforms easily detect multiple views from same IP
- ❌ Views likely to be filtered out as invalid
- ❌ Risk of IP ban after too many requests

### With Proxies
When using proxy rotation:
- ✅ Each session uses a DIFFERENT IP address
- ✅ Appears like views from different users/locations
- ✅ Much harder to detect as automated
- ✅ Higher success rate for view counting
- ✅ Distribute load across multiple IPs

**Bottom Line**: Proxies are essential for running more than a few sessions effectively.

---

## How Proxy Rotation Works

### Sequential Rotation (Default)
```
Session 1: Proxy 1 (IP: 1.1.1.1)
Session 2: Proxy 2 (IP: 2.2.2.2)
Session 3: Proxy 3 (IP: 3.3.3.3)
Session 4: Proxy 1 (IP: 1.1.1.1) ← cycles back
```

**Best for**: Consistent, predictable rotation

### Random Rotation
```
Session 1: Proxy 2 (IP: 2.2.2.2)
Session 2: Proxy 1 (IP: 1.1.1.1)
Session 3: Proxy 3 (IP: 3.3.3.3)
Session 4: Proxy 2 (IP: 2.2.2.2) ← random
```

**Best for**: More unpredictable patterns

### How the Bot Uses Proxies

1. **Before Session 1**: Loads first proxy → Opens Chrome with that proxy
2. **After Session 1**: Closes Chrome
3. **Before Session 2**: Loads next proxy → Opens new Chrome with new proxy
4. **Repeat** for all sessions

This ensures each session truly uses a different IP address.

---

## Setting Up Proxies

### Method 1: Using proxies.txt (Recommended)

1. **Create/Edit proxies.txt** in the project folder
2. **Add proxies** (one per line):
```
http://185.199.228.220:7300
http://185.199.229.156:7492
http://username:password@premium-proxy.com:8080
192.168.1.100:8080
socks5://10.0.0.1:1080
```

3. **Comments & blank lines** are ignored:
```
# These are my datacenter proxies
http://185.199.228.220:7300

# Premium residential proxies
http://user:pass@premium.com:8080
```

4. **Run the bot**:
```
Use proxy rotation? (y/n): y
Enter '1' to load from file or '2' to enter manually: 1
Enter proxy file path (default: proxies.txt): [press Enter]
```

### Method 2: Manual Entry

1. **Run the bot**
2. **Choose manual entry**:
```
Use proxy rotation? (y/n): y
Enter '1' to load from file or '2' to enter manually: 2
```

3. **Enter proxies** one by one:
```
Enter proxies (one per line, empty line to finish):
Proxy: http://proxy1.com:8080
Proxy: http://proxy2.com:8080
Proxy: [press Enter to finish]
```

### Method 3: Programmatic Usage

```python
from youtube_refresher import MultiPlatformViewBot

proxies = [
    "http://185.199.228.220:7300",
    "http://185.199.229.156:7492",
    "http://user:pass@premium.com:8080"
]

bot = MultiPlatformViewBot(
    youtube_url="https://youtube.com/watch?v=VIDEO_ID",
    session_count=10,
    proxy_list=proxies,
    rotate_proxy_each_session=True  # Sequential rotation
)

bot.run()
```

---

## Proxy Formats

The bot supports multiple proxy formats:

### 1. IP:Port (Basic)
```
185.199.228.220:7300
```
- Simplest format
- Automatically treated as HTTP proxy
- No authentication

### 2. HTTP/HTTPS Protocol
```
http://185.199.228.220:7300
https://185.199.228.220:7300
```
- Explicitly specifies protocol
- Recommended for clarity

### 3. Authenticated HTTP Proxy
```
http://username:password@proxy.example.com:8080
```
- Includes username and password
- For premium proxy services
- Credentials are masked in logs (shows `***:***@ip:port`)

### 4. SOCKS5 Proxy
```
socks5://proxy.example.com:1080
```
- SOCKS5 protocol support
- Often faster for certain use cases

### Examples by Provider

**Bright Data (formerly Luminati):**
```
http://username-session-random123:password@zproxy.lum-superproxy.io:22225
```

**Smartproxy:**
```
http://user:pass@gate.smartproxy.com:7000
```

**Generic Datacenter:**
```
http://185.199.228.220:7300
```

---

## Finding Proxy Providers

### Free Proxies (Testing Only)

**Pros:**
- Free to use
- Good for initial testing

**Cons:**
- ❌ Very unreliable (90% don't work)
- ❌ Slow speeds
- ❌ Often already blacklisted by YouTube/TikTok
- ❌ Security risks
- ❌ May log your data

**Sources:**
- [Free Proxy List](https://free-proxy-list.net/)
- [ProxyScrape](https://proxyscrape.com/free-proxy-list)
- [GeoNode](https://geonode.com/free-proxy-list)

**Not recommended for actual use** - only for testing the bot functionality.

### Paid Proxies (Recommended)

#### Residential Proxies (Best for View Bots)

**What they are:** Real IPs from real devices (homes, phones)

**Pros:**
- ✅ Highest success rate
- ✅ Hardest to detect
- ✅ Less likely to be blocked
- ✅ Look like real users

**Cons:**
- 💰 More expensive ($5-15 per GB)
- Slower than datacenter

**Top Providers:**
1. **Bright Data** - Premium quality, expensive
   - https://brightdata.com/
   - $5-15/GB
   
2. **Smartproxy** - Good balance of price/quality
   - https://smartproxy.com/
   - $7-12/GB
   
3. **Oxylabs** - Enterprise-grade
   - https://oxylabs.io/
   - $8-15/GB

4. **IPRoyal** - Budget-friendly
   - https://iproyal.com/
   - $2-7/GB

#### Datacenter Proxies (Budget Option)

**What they are:** IPs from data centers, not real devices

**Pros:**
- ✅ Much cheaper ($1-3 per proxy/month)
- ✅ Very fast speeds
- ✅ Good for high-volume

**Cons:**
- ⚠️ Easier to detect
- ⚠️ Higher block rate
- ⚠️ Less "human-like"

**Providers:**
- **ProxyEmpire**
- **HighProxies**
- **MyPrivateProxy**

### How Many Proxies Do You Need?

**Minimum:** 5-10 proxies
- Enough for basic rotation
- Can cycle through them

**Recommended:** 20-50 proxies
- Better distribution
- Less reuse of same IP

**Optimal:** 1 proxy per session
- Each session = unique IP
- Maximum effectiveness
- Most expensive

**Formula:**
```
Proxies needed = Total sessions ÷ How many times you want to reuse each proxy
```

Example: 100 sessions, reuse each proxy 5 times = 20 proxies

---

## Testing Proxies

### Test Before Running Bot

Always test proxies before adding them:

```python
import requests

proxy = "http://proxy.example.com:8080"

try:
    response = requests.get(
        "http://ipinfo.io/json",
        proxies={"http": proxy, "https": proxy},
        timeout=10
    )
    print(f"✓ Proxy works! IP: {response.json()['ip']}")
except Exception as e:
    print(f"✗ Proxy failed: {str(e)}")
```

### Check IP Location

Verify proxy location matches expectations:

```python
response = requests.get(
    "http://ipinfo.io/json",
    proxies={"http": proxy, "https": proxy}
)

data = response.json()
print(f"IP: {data['ip']}")
print(f"Location: {data['city']}, {data['country']}")
```

### Test with YouTube

```python
response = requests.get(
    "https://www.youtube.com",
    proxies={"http": proxy, "https": proxy},
    timeout=15
)

if response.status_code == 200:
    print("✓ Proxy works with YouTube!")
else:
    print(f"✗ YouTube blocked: {response.status_code}")
```

---

## Troubleshooting

### Proxy Connection Failed

**Error:**
```
[!] Error: Proxy connection failed
```

**Solutions:**
1. ✅ Verify proxy format is correct
2. ✅ Check if proxy requires authentication
3. ✅ Test proxy with simple request first
4. ✅ Contact provider if premium proxy
5. ✅ Try different proxy from your list

### Proxy Timeout

**Error:**
```
TimeoutError: Proxy took too long to respond
```

**Solutions:**
1. ✅ Proxy server might be down
2. ✅ Try increasing timeout in code
3. ✅ Use faster proxies (datacenter vs residential)
4. ✅ Remove slow proxies from list

### YouTube/TikTok Blocks Proxy

**Issue:** Videos won't load or immediate errors

**Solutions:**
1. ✅ Proxy IP is blacklisted - get new proxies
2. ✅ Use residential proxies instead of datacenter
3. ✅ Rotate proxies more frequently
4. ✅ Add delays between sessions

### Authentication Failed

**Error:**
```
407 Proxy Authentication Required
```

**Solutions:**
1. ✅ Verify username:password is correct
2. ✅ Format: `http://user:pass@ip:port`
3. ✅ URL encode special characters in password
4. ✅ Check with provider for correct credentials

---

## Best Practices

### 1. Quality Over Quantity
- Better to have 10 working proxies than 100 dead ones
- Test all proxies before adding to list
- Remove non-working proxies immediately

### 2. Rotate Properly
- Don't reuse same proxy too quickly
- Wait at least 5-10 minutes before reusing
- Use sequential rotation for even distribution

### 3. Monitor Proxy Health
- Keep track of which proxies work best
- Replace failing proxies promptly
- Test new proxies before adding

### 4. Mix Proxy Types
- Combine residential and datacenter
- Use residential for important sessions
- Use datacenter for bulk/testing

### 5. Stay Within Provider Limits
- Don't exceed bandwidth limits
- Respect concurrent connection limits
- Monitor usage to avoid overages

### 6. Security
- Don't share proxy credentials
- Use HTTPS proxies when possible
- Clear proxy lists from logs
- Secure proxies.txt file

### 7. Geographic Distribution
- Use proxies from different countries
- Match proxy location to target audience
- Avoid suspicious patterns (all from same location)

### 8. Session Spacing
- Add delays between sessions (5-15 seconds)
- Don't blast through all proxies rapidly
- Mimic natural user behavior

---

## Example Configuration

### Small Scale (Testing)
```
Proxies: 5-10
Sessions: 10-20
Proxy reuse: 2-4 times each
Cost: $10-20/month (datacenter)
```

### Medium Scale
```
Proxies: 20-50
Sessions: 50-100
Proxy reuse: 2-3 times each
Cost: $50-100/month (mix)
```

### Large Scale
```
Proxies: 100+
Sessions: 200-500
Proxy reuse: 1-2 times each
Cost: $200-500/month (residential)
```

---

## Summary Checklist

Before running with proxies:

- [ ] Obtained working proxies (free or paid)
- [ ] Tested proxies individually
- [ ] Added proxies to `proxies.txt` (one per line)
- [ ] Verified format is correct
- [ ] Set appropriate session count
- [ ] Configured rotation mode (sequential/random)
- [ ] Ready to run bot!

---

**Remember:** Proxy rotation significantly improves effectiveness but doesn't guarantee views won't be filtered. Platforms use many factors beyond just IP addresses for detection.

**Stay ethical, stay safe! 🛡️**

