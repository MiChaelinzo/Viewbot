# Multi-Platform View Bot (YouTube + TikTok)

**⚠️ DISCLAIMER: This tool is for experimental and educational purposes only. Artificially generating views violates YouTube's and TikTok's Terms of Service and may result in account suspension or other penalties.**

## Description

This Python script automates the process of browsing and watching content on YouTube and TikTok in Chrome. It uses `undetected-chromedriver` to avoid basic bot detection mechanisms and simulates realistic human browsing patterns by alternating between platforms.

## Features

### Multi-Platform Support
- **YouTube**: Opens and watches videos with realistic viewing patterns
- **TikTok**: Browses creator profiles and watches multiple videos in sequence
- **Cross-Platform Rotation**: Alternates between YouTube and TikTok to simulate natural browsing

### Human-Like Behavior
- Random watch durations (adjustable ranges)
- Random scroll actions to simulate engagement
- Realistic breaks between sessions
- Variable engagement patterns (comments, pauses, etc.)

### Advanced Features
- **Proxy Rotation**: Use different IP addresses for each session
- Auto-skips YouTube ads when possible
- TikTok creator profile crawling (watches multiple videos from a creator)
- Configurable session counts and watch times
- Uses undetected-chromedriver to avoid basic detection
- Weighted platform selection (customize YouTube vs TikTok ratio)
- Support for authenticated proxies (username:password)

## Requirements

- Python 3.7 or higher
- Google Chrome browser installed
- Internet connection

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python youtube_refresher.py
```

The script will prompt you for:
1. **YouTube video URL** (optional - leave blank to skip)
2. **TikTok URL** - either a specific video or creator profile (optional - leave blank to skip)
   - You can enter just `@username` for a creator profile
   - Or provide full URLs like `https://www.tiktok.com/@username` or `https://www.tiktok.com/@username/video/123456789`
3. **Proxy rotation** (optional but recommended)
   - Load from file (`proxies.txt`)
   - Enter manually
   - Skip to use your real IP
4. **Number of browsing sessions** (default: 10)

### Examples

#### YouTube Only
```
YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
TikTok URL: [leave blank]
Number of browsing sessions: 5
```

#### TikTok Only (Creator Profile)
```
YouTube video URL: [leave blank]
TikTok URL: @username
Number of browsing sessions: 10
```

#### Both Platforms (Most Realistic)
```
YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
TikTok URL: @username
Number of browsing sessions: 15
```
The bot will randomly alternate between platforms (~60% YouTube, ~40% TikTok)

## Proxy Rotation Setup

### Why Use Proxies?

Proxies are **highly recommended** for avoiding detection:
- Each session uses a different IP address
- Appears like views from different users/locations
- Harder for platforms to detect as automated traffic
- Essential for running multiple sessions

### Setting Up Proxies

#### Option 1: Using a Proxy File (Recommended)

1. Create or edit `proxies.txt` in the project directory
2. Add one proxy per line:
```
http://proxy1.example.com:8080
http://proxy2.example.com:3128
http://username:password@premium-proxy.com:8080
192.168.1.1:8080
```

3. Run the script and choose option `1` (load from file)

#### Option 2: Manual Entry

1. Run the script
2. When prompted, choose `y` for proxy rotation
3. Select option `2` (enter manually)
4. Enter proxies one by one, press Enter on empty line when done

### Supported Proxy Formats

- `ip:port` - Basic HTTP proxy
- `http://ip:port` - HTTP proxy with protocol
- `http://user:pass@ip:port` - Authenticated HTTP proxy
- `socks5://ip:port` - SOCKS5 proxy

### Where to Get Proxies?

**Free Proxies (Not Recommended):**
- Usually slow, unreliable, and often blocked
- Good for testing only
- Sources: Free proxy lists online

**Paid Proxies (Recommended):**
- Residential proxies (best, looks like real users)
- Datacenter proxies (cheaper, less reliable)
- Providers: Bright Data, Smartproxy, Oxylabs, etc.

### Proxy Rotation Modes

- **Sequential** (default): Cycles through proxies in order
- **Random**: Picks random proxy for each session

### Need More Help?

📚 **See [PROXY_GUIDE.md](PROXY_GUIDE.md) for complete proxy documentation:**
- Detailed setup instructions
- Testing proxies
- Troubleshooting common issues
- Provider recommendations
- Best practices

## How It Works

### YouTube Sessions
1. Opens the specified YouTube video
2. Attempts to skip ads automatically
3. Watches for a random duration (30-90 seconds by default)
4. Performs random scroll actions to simulate engagement
5. Occasionally scrolls to comments section

### TikTok Sessions
1. Navigates to TikTok URL (video or creator profile)
2. If creator profile:
   - Scrolls through the profile to load videos
   - Collects available video links (up to 5)
   - Watches 2-5 random videos from the creator
3. If single video:
   - Watches the video for 20-50 seconds
4. Random scrolling and engagement simulation

### Multi-Platform Flow
1. Opens Chrome using undetected-chromedriver
2. Randomly selects a platform for each session (weighted: 60% YouTube, 40% TikTok)
3. Executes platform-specific browsing behavior
4. Takes random breaks between sessions (5-15 seconds)
5. Repeats for the configured number of sessions

## Important Notes

### Platform Detection Systems

Both YouTube and TikTok use sophisticated algorithms to detect and filter artificial engagement:

**Detection Methods:**
- IP address tracking
- Browser fingerprinting
- Watch time analysis
- User behavior patterns
- Device information
- Account history
- Cross-platform tracking

**Why Multi-Platform Browsing Helps (Theoretically):**
- Mimics real user behavior (people browse multiple platforms)
- More varied browsing patterns
- Harder to detect as pure "view botting"
- Creates more realistic session data

### Limitations

- **Detection Still Likely**: While this script uses techniques to appear more human-like (platform rotation, random delays, varied watch times), both platforms have highly advanced detection systems
- **No Guarantee**: Views may still be filtered or flagged as invalid
- **Account Risk**: Using automation tools can result in account bans

### Ethical & Legal Considerations

⚠️ **Manipulating view/engagement counts violates Terms of Service and may be considered fraud**

**Potential Consequences:**
- Video/content removal
- Account/channel termination
- Legal action
- Platform-wide bans

**This tool is for educational purposes only to understand how automation works. Do not use it to artificially inflate metrics.**

## Customization

You can modify the following parameters in the script:

### Timing Parameters
- `watch_duration_range` in `watch_content()`: Tuple defining min/max watch time in seconds
  - YouTube default: (30, 90)
  - TikTok default: (15, 45) for individual videos, (20, 50) for single video
- `video_count_range` in `watch_tiktok_session()`: How many TikTok videos to watch (2, 5)
- Break time between sessions: Currently (5, 15) seconds

### Platform Weighting
In the `run()` method, line ~249:
```python
weights = [0.6, 0.4]  # 60% YouTube, 40% TikTok
```
Adjust these weights to change the platform distribution.

### Browser Options
In `setup_driver()` method, you can add more Chrome options:
- Window size
- User agent
- Extensions
- Proxy settings (for advanced use)

## Troubleshooting

### Common Issues

**Chrome driver version mismatch:**
```bash
pip install --upgrade undetected-chromedriver
```

**TikTok videos not loading:**
- TikTok's page structure changes frequently
- The script uses multiple selectors to find videos
- Some regions may have different TikTok layouts

**Views not counting:**
- Remember: platforms use sophisticated detection
- Try increasing watch times
- Add more randomization
- Consider using actual accounts (not recommended)

**Script crashes:**
- Make sure Chrome is up to date
- Check your internet connection
- Ensure URLs are valid and accessible

## Quick Start (Windows)

For Windows users, simply double-click `run.bat` to:
1. Check Python installation
2. Install dependencies automatically
3. Start the bot

## Programmatic Usage

See `example_usage.py` for examples of using the bot in your own Python scripts without interactive prompts.

## Files Overview

- `youtube_refresher.py` - Main bot script
- `requirements.txt` - Python dependencies
- `proxies.txt` - Proxy list file (add your proxies here)
- `run.bat` - Windows launcher script
- `example_usage.py` - Programmatic usage examples
- `README.md` - This file (comprehensive documentation)
- `QUICK_START.md` - Quick reference guide
- `PROXY_GUIDE.md` - Complete proxy setup and troubleshooting guide
- `.gitignore` - Git ignore configuration

## Legal Notice

This tool is provided for educational purposes only. The author is not responsible for any misuse or violations of Terms of Service. Use at your own risk.

## Future Enhancement Ideas

Want to make this even more sophisticated? Consider adding:
- ✅ **Proxy rotation** - ✅ IMPLEMENTED! Use different IPs for each session
- **Multiple videos** - Rotate through several target videos
- **Search-based navigation** - Search for videos instead of direct URLs
- **Account login** - Sign in to make behavior more "legitimate"
- **Variable user agents** - Rotate browser fingerprints
- **Playlist support** - Navigate through playlists
- **Mobile emulation** - Simulate mobile device browsing
- **CAPTCHA solving** - Integrate with CAPTCHA solving services
- **Headless mode** - Run without visible browser window
- **View duration variation** - Watch different percentages of videos

