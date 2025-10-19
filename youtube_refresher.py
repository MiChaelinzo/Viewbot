import undetected_chromedriver as uc
import time
import random
from datetime import datetime
from urllib.parse import urlparse

class MultiPlatformViewBot:
    def __init__(self, youtube_url=None, tiktok_url=None, session_count=10, proxy_list=None, rotate_proxy_each_session=True):
        """
        Initialize the Multi-Platform View Bot
        
        Args:
            youtube_url (str): The YouTube video URL to refresh
            tiktok_url (str): TikTok video or creator channel URL
            session_count (int): Number of browsing sessions to perform
            proxy_list (list): List of proxy servers in format 'http://ip:port' or 'user:pass@ip:port'
            rotate_proxy_each_session (bool): If True, rotates proxy for each session. If False, uses random proxy
        """
        self.youtube_url = youtube_url
        self.tiktok_url = tiktok_url
        self.session_count = session_count
        self.proxy_list = proxy_list or []
        self.rotate_proxy_each_session = rotate_proxy_each_session
        self.current_proxy_index = 0
        self.driver = None
        
    def get_next_proxy(self):
        """
        Get the next proxy from the list
        
        Returns:
            str: Proxy URL or None if no proxies available
        """
        if not self.proxy_list:
            return None
        
        if self.rotate_proxy_each_session:
            # Sequential rotation
            proxy = self.proxy_list[self.current_proxy_index]
            self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxy_list)
        else:
            # Random selection
            proxy = random.choice(self.proxy_list)
        
        return proxy
    
    def setup_driver(self, proxy=None):
        """
        Setup undetected Chrome driver with options
        
        Args:
            proxy (str): Proxy server in format 'http://ip:port' or 'http://user:pass@ip:port'
        """
        options = uc.ChromeOptions()
        
        # Add arguments to make the browser appear more human-like
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        
        # Add proxy if provided
        if proxy:
            print(f"[*] Using proxy: {self._mask_proxy(proxy)}")
            
            # Handle different proxy formats
            if '@' in proxy:
                # Format: http://user:pass@ip:port
                options.add_argument(f'--proxy-server={proxy}')
            else:
                # Format: http://ip:port or ip:port
                if not proxy.startswith('http'):
                    proxy = f'http://{proxy}'
                options.add_argument(f'--proxy-server={proxy}')
        
        # Use undetected-chromedriver to avoid detection
        self.driver = uc.Chrome(options=options)
        
        # Set reasonable timeouts
        self.driver.set_page_load_timeout(30)
    
    def _mask_proxy(self, proxy):
        """Mask proxy credentials for display"""
        if '@' in proxy:
            # Hide credentials
            parts = proxy.split('@')
            return f"***:***@{parts[1]}"
        return proxy
    
    def restart_driver_with_new_proxy(self):
        """Close current driver and start a new one with a different proxy"""
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            time.sleep(2)
        
        proxy = self.get_next_proxy()
        self.setup_driver(proxy=proxy)
        
    def detect_platform(self, url):
        """Detect which platform the URL belongs to"""
        if 'youtube.com' in url or 'youtu.be' in url:
            return 'youtube'
        elif 'tiktok.com' in url:
            return 'tiktok'
        else:
            return 'unknown'
    
    def watch_content(self, platform, watch_duration_range=(30, 90)):
        """
        Watch content for a random duration to simulate human behavior
        
        Args:
            platform (str): 'youtube' or 'tiktok'
            watch_duration_range (tuple): Min and max seconds to watch
        """
        watch_time = random.randint(watch_duration_range[0], watch_duration_range[1])
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Watching {platform} content for {watch_time} seconds...")
        
        # Add small random scrolls to simulate engagement
        scroll_count = random.randint(1, 3)
        interval = watch_time / (scroll_count + 1)
        
        for i in range(scroll_count):
            time.sleep(random.uniform(interval * 0.8, interval * 1.2))
            scroll_amount = random.randint(-300, 300)
            try:
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            except:
                pass
        
        # Wait for remaining time
        time.sleep(interval)
    
    def get_tiktok_creator_videos(self):
        """
        Attempt to find and collect TikTok video links from a creator's page
        
        Returns:
            list: List of video URLs found on the page
        """
        videos = []
        try:
            time.sleep(random.uniform(3, 5))
            
            # Scroll down to load more videos
            for _ in range(random.randint(2, 4)):
                self.driver.execute_script("window.scrollBy(0, 800);")
                time.sleep(random.uniform(1, 2))
            
            # Find video links on the page
            # TikTok structure may vary, so we try multiple selectors
            selectors = [
                "a[href*='/video/']",
                "div[data-e2e='user-post-item'] a",
                "div.tiktok-video-item a"
            ]
            
            for selector in selectors:
                try:
                    elements = self.driver.find_elements("css selector", selector)
                    for elem in elements[:10]:  # Get up to 10 videos
                        href = elem.get_attribute('href')
                        if href and '/video/' in href and href not in videos:
                            videos.append(href)
                except:
                    continue
            
            print(f"[*] Found {len(videos)} TikTok videos on creator page")
        except Exception as e:
            print(f"[!] Error finding TikTok videos: {str(e)}")
        
        return videos[:5]  # Return max 5 videos
    
    def watch_tiktok_session(self, start_url, video_count_range=(2, 5)):
        """
        Watch multiple TikTok videos in a session
        
        Args:
            start_url (str): Initial TikTok URL (video or creator page)
            video_count_range (tuple): Min and max number of videos to watch
        """
        print(f"\n[TikTok] Starting TikTok session from: {start_url}")
        
        try:
            # Navigate to the TikTok URL
            self.driver.get(start_url)
            time.sleep(random.uniform(4, 7))
            
            # Check if it's a creator page or single video
            is_creator_page = '/@' in start_url and '/video/' not in start_url
            
            if is_creator_page:
                print("[*] Detected creator page, collecting videos...")
                video_urls = self.get_tiktok_creator_videos()
                
                if video_urls:
                    # Watch random selection of creator's videos
                    videos_to_watch = random.randint(video_count_range[0], min(video_count_range[1], len(video_urls)))
                    selected_videos = random.sample(video_urls, min(videos_to_watch, len(video_urls)))
                    
                    for idx, video_url in enumerate(selected_videos, 1):
                        print(f"\n[TikTok Video {idx}/{len(selected_videos)}] Navigating to: {video_url}")
                        self.driver.get(video_url)
                        time.sleep(random.uniform(2, 4))
                        self.watch_content('tiktok', watch_duration_range=(15, 45))
                        
                        # Random chance to scroll comments
                        if random.random() > 0.5:
                            self.driver.execute_script("window.scrollBy(0, 400);")
                            time.sleep(random.uniform(1, 3))
                else:
                    # If no videos found, just watch the creator page
                    self.watch_content('tiktok', watch_duration_range=(20, 40))
            else:
                # Single video - just watch it
                print("[*] Watching single TikTok video")
                self.watch_content('tiktok', watch_duration_range=(20, 50))
                
        except Exception as e:
            print(f"[!] Error during TikTok session: {str(e)}")
    
    def watch_youtube_video(self):
        """Watch YouTube video with ad handling"""
        print(f"\n[YouTube] Navigating to: {self.youtube_url}")
        
        try:
            self.driver.get(self.youtube_url)
            time.sleep(random.uniform(3, 6))
            
            # Try to skip ads
            self.skip_youtube_ad()
            
            # Watch the video
            self.watch_content('youtube', watch_duration_range=(30, 90))
            
            # Random engagement actions
            if random.random() > 0.7:
                # Scroll to comments
                self.driver.execute_script("window.scrollTo(0, 600);")
                time.sleep(random.uniform(2, 4))
                
        except Exception as e:
            print(f"[!] Error during YouTube session: {str(e)}")
    
    def skip_youtube_ad(self):
        """Attempt to skip YouTube ads"""
        try:
            time.sleep(5)
            skip_selectors = [
                ".ytp-ad-skip-button",
                ".ytp-skip-ad-button",
                "button.ytp-ad-skip-button-modern"
            ]
            
            for selector in skip_selectors:
                try:
                    skip_button = self.driver.find_elements("css selector", selector)
                    if skip_button and skip_button[0].is_displayed():
                        skip_button[0].click()
                        print("[*] Skipped YouTube ad")
                        time.sleep(1)
                        return
                except:
                    continue
        except:
            pass
    
    def run(self):
        """Main function to run the multi-platform bot"""
        try:
            print("=" * 60)
            print("Multi-Platform View Bot (YouTube + TikTok)")
            print("=" * 60)
            
            # Display configuration
            if self.youtube_url:
                print(f"YouTube URL: {self.youtube_url}")
            if self.tiktok_url:
                print(f"TikTok URL: {self.tiktok_url}")
            print(f"Session Count: {self.session_count}")
            
            # Display proxy configuration
            if self.proxy_list:
                print(f"Proxy Rotation: Enabled ({len(self.proxy_list)} proxies)")
                print(f"Rotation Mode: {'Sequential' if self.rotate_proxy_each_session else 'Random'}")
            else:
                print("Proxy Rotation: Disabled (using your real IP)")
            
            print("=" * 60)
            
            # Validate that at least one URL is provided
            if not self.youtube_url and not self.tiktok_url:
                print("[!] Error: Please provide at least one URL (YouTube or TikTok)")
                return
            
            # Setup the driver with initial proxy
            print("\n[*] Setting up Chrome driver...")
            initial_proxy = self.get_next_proxy() if self.proxy_list else None
            self.setup_driver(proxy=initial_proxy)
            
            # Create browsing pattern
            # Mix of both platforms if both are provided
            platforms_available = []
            if self.youtube_url:
                platforms_available.append('youtube')
            if self.tiktok_url:
                platforms_available.append('tiktok')
            
            # Main browsing loop
            for i in range(self.session_count):
                print(f"\n{'='*60}")
                print(f"Session {i + 1}/{self.session_count}")
                print(f"{'='*60}")
                
                # Rotate proxy for each session (except first)
                if self.proxy_list and i > 0:
                    print("[*] Rotating to new proxy...")
                    self.restart_driver_with_new_proxy()
                
                # Decide which platform to visit
                if len(platforms_available) == 2:
                    # Random weighted choice - favor the platform we want to boost
                    # 60% YouTube, 40% TikTok (can be adjusted)
                    weights = [0.6, 0.4]
                    platform = random.choices(platforms_available, weights=weights)[0]
                else:
                    platform = platforms_available[0]
                
                print(f"[*] Selected platform: {platform.upper()}")
                
                # Visit the selected platform
                if platform == 'youtube':
                    self.watch_youtube_video()
                elif platform == 'tiktok':
                    self.watch_tiktok_session(self.tiktok_url)
                
                # Add break between sessions (except last one)
                if i < self.session_count - 1:
                    break_time = random.uniform(5, 15)
                    print(f"\n[*] Taking a {break_time:.1f}s break before next session...")
                    time.sleep(break_time)
            
            print(f"\n{'='*60}")
            print(f"[✓] Completed all {self.session_count} sessions!")
            print("=" * 60)
            print("\n[*] Keeping browser open. Press Ctrl+C to close...")
            
            # Keep the browser open
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n[*] Interrupted by user")
        except Exception as e:
            print(f"\n[!] Error occurred: {str(e)}")
            import traceback
            traceback.print_exc()
        finally:
            if self.driver:
                print("[*] Closing browser...")
                self.driver.quit()

def load_proxies_from_file(filepath):
    """Load proxies from a text file (one proxy per line)"""
    try:
        with open(filepath, 'r') as f:
            proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return proxies
    except FileNotFoundError:
        print(f"[!] Error: Proxy file '{filepath}' not found")
        return []
    except Exception as e:
        print(f"[!] Error reading proxy file: {str(e)}")
        return []

if __name__ == "__main__":
    # Example usage
    print("\n" + "=" * 60)
    print("Multi-Platform View Bot - Experimental Tool")
    print("=" * 60)
    print("\nNOTE: This is for experimental/educational purposes only.")
    print("Artificial view generation violates platform Terms of Service.")
    print("=" * 60 + "\n")
    
    # Get YouTube URL from user
    print("Enter URLs (leave blank to skip a platform):\n")
    youtube_url = input("YouTube video URL: ").strip()
    
    # Validate YouTube URL if provided
    if youtube_url and "youtube.com" not in youtube_url and "youtu.be" not in youtube_url:
        print("[!] Invalid YouTube URL. Please provide a valid YouTube video link.")
        exit(1)
    
    # Get TikTok URL from user
    tiktok_url = input("TikTok URL (video or creator profile like @username): ").strip()
    
    # Validate TikTok URL if provided
    if tiktok_url:
        # If user entered just @username, convert to full URL
        if tiktok_url.startswith('@'):
            tiktok_url = f"https://www.tiktok.com/{tiktok_url}"
        elif "tiktok.com" not in tiktok_url:
            print("[!] Invalid TikTok URL. Please provide a valid TikTok link or @username.")
            exit(1)
    
    # Check if at least one URL is provided
    if not youtube_url and not tiktok_url:
        print("[!] Error: Please provide at least one URL (YouTube or TikTok)")
        exit(1)
    
    # Proxy configuration
    print("\n" + "=" * 60)
    print("Proxy Configuration (Optional)")
    print("=" * 60)
    print("Using proxies helps avoid IP-based detection by rotating IPs.")
    print("Formats supported:")
    print("  - ip:port (e.g., 192.168.1.1:8080)")
    print("  - http://ip:port")
    print("  - http://user:pass@ip:port (authenticated)")
    print("=" * 60 + "\n")
    
    use_proxies = input("Use proxy rotation? (y/n): ").strip().lower()
    proxy_list = []
    
    if use_proxies == 'y':
        proxy_method = input("\nEnter '1' to load from file or '2' to enter manually: ").strip()
        
        if proxy_method == '1':
            proxy_file = input("Enter proxy file path (default: proxies.txt): ").strip() or "proxies.txt"
            proxy_list = load_proxies_from_file(proxy_file)
            
            if proxy_list:
                print(f"[✓] Loaded {len(proxy_list)} proxies from {proxy_file}")
            else:
                print("[!] No proxies loaded. Continuing without proxies.")
                
        elif proxy_method == '2':
            print("\nEnter proxies (one per line, empty line to finish):")
            while True:
                proxy = input("Proxy: ").strip()
                if not proxy:
                    break
                proxy_list.append(proxy)
            
            if proxy_list:
                print(f"[✓] Added {len(proxy_list)} proxies")
        else:
            print("[!] Invalid choice. Continuing without proxies.")
    
    # Get session count
    try:
        session_count = int(input("\nEnter number of browsing sessions (default 10): ").strip() or "10")
    except ValueError:
        session_count = 10
    
    print("\n" + "=" * 60)
    print("Configuration Summary:")
    print("=" * 60)
    if youtube_url:
        print(f"✓ YouTube: {youtube_url}")
    if tiktok_url:
        print(f"✓ TikTok: {tiktok_url}")
    print(f"✓ Sessions: {session_count}")
    
    if proxy_list:
        print(f"✓ Proxy Rotation: Enabled ({len(proxy_list)} proxies)")
    else:
        print("✓ Proxy Rotation: Disabled")
    
    if youtube_url and tiktok_url:
        print("\n[*] Both platforms configured - will randomly alternate")
        print("[*] YouTube sessions: ~60% | TikTok sessions: ~40%")
    
    print("=" * 60)
    
    confirm = input("\nStart browsing? (y/n): ").strip().lower()
    if confirm != 'y':
        print("[*] Cancelled by user")
        exit(0)
    
    # Create and run the bot
    bot = MultiPlatformViewBot(
        youtube_url=youtube_url if youtube_url else None,
        tiktok_url=tiktok_url if tiktok_url else None,
        session_count=session_count,
        proxy_list=proxy_list if proxy_list else None,
        rotate_proxy_each_session=True  # Sequential rotation by default
    )
    bot.run()

