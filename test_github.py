import requests

def get_github_user(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"User '{username}' not found or GitHub API error"}
    
    data = response.json()
    
    return {
        "name": data.get("name"),
        "bio": data.get("bio"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "profile_url": data.get("html_url"),
    }

# quick test
if __name__ == "__main__":
    result = get_github_user("torvalds")  # Linus Torvalds' GitHub, has tons of public data
    print(result)