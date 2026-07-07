from mcp.server.fastmcp import FastMCP
import requests

# Create the MCP server, give it a name
mcp = FastMCP("github-stats")

@mcp.tool()
def get_github_user(username: str) -> dict:
    """Get public GitHub profile stats for a given username.
    
    Args:
        username: The GitHub username to look up
    """
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

if __name__ == "__main__":
    mcp.run()