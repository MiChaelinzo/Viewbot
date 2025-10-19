"""
Example usage of the Multi-Platform View Bot

This file shows how to use the bot programmatically instead of
using the interactive prompts.
"""

from youtube_refresher import MultiPlatformViewBot

# Example 1: YouTube only
def youtube_only_example():
    print("\n=== Example 1: YouTube Only ===")
    bot = MultiPlatformViewBot(
        youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        tiktok_url=None,
        session_count=5
    )
    bot.run()


# Example 2: TikTok only (creator profile)
def tiktok_only_example():
    print("\n=== Example 2: TikTok Only ===")
    bot = MultiPlatformViewBot(
        youtube_url=None,
        tiktok_url="https://www.tiktok.com/@username",  # Replace with actual username
        session_count=5
    )
    bot.run()


# Example 3: Both platforms (recommended for most realistic behavior)
def both_platforms_example():
    print("\n=== Example 3: Both Platforms ===")
    bot = MultiPlatformViewBot(
        youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        tiktok_url="https://www.tiktok.com/@username",  # Replace with actual username
        session_count=10
    )
    bot.run()


# Example 4: Using proxy rotation
def proxy_rotation_example():
    print("\n=== Example 4: Proxy Rotation ===")
    
    # List of proxy servers
    proxies = [
        "http://proxy1.example.com:8080",
        "http://proxy2.example.com:8080",
        "http://username:password@proxy3.example.com:8080",
    ]
    
    bot = MultiPlatformViewBot(
        youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        tiktok_url="https://www.tiktok.com/@username",
        session_count=10,
        proxy_list=proxies,
        rotate_proxy_each_session=True  # Use sequential rotation
    )
    bot.run()


# Example 5: Loading proxies from file
def proxy_from_file_example():
    print("\n=== Example 5: Proxies from File ===")
    
    from youtube_refresher import load_proxies_from_file
    
    # Load proxies from proxies.txt
    proxies = load_proxies_from_file("proxies.txt")
    
    if not proxies:
        print("[!] No proxies loaded. Please add proxies to proxies.txt")
        return
    
    print(f"[✓] Loaded {len(proxies)} proxies")
    
    bot = MultiPlatformViewBot(
        youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        tiktok_url=None,
        session_count=len(proxies),  # One session per proxy
        proxy_list=proxies,
        rotate_proxy_each_session=True
    )
    bot.run()


if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     Multi-Platform View Bot - Example Usage             ║
    ╚══════════════════════════════════════════════════════════╝
    
    Choose an example to run:
    
    1. YouTube only
    2. TikTok only  
    3. Both platforms (recommended)
    4. Using proxy rotation (manual list)
    5. Using proxy rotation (from file)
    
    Note: Edit this file to add your actual URLs/proxies before running!
    """)
    
    choice = input("Enter choice (1-5): ").strip()
    
    examples = {
        "1": youtube_only_example,
        "2": tiktok_only_example,
        "3": both_platforms_example,
        "4": proxy_rotation_example,
        "5": proxy_from_file_example
    }
    
    if choice in examples:
        if choice in ["4", "5"]:
            print("\n⚠️  Make sure you've configured proxies in example_usage.py or proxies.txt!")
        else:
            print("\n⚠️  Make sure you've edited the URLs in example_usage.py first!")
        
        confirm = input("Continue? (y/n): ").strip().lower()
        if confirm == 'y':
            examples[choice]()
        else:
            print("Cancelled.")
    else:
        print("Invalid choice!")

