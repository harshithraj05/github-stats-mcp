# GitHub Stats MCP Server

A simple MCP (Model Context Protocol) server that lets Claude fetch live public GitHub profile stats for any username.

Built as a learning project to understand how MCP works — how an AI assistant like Claude can discover and call external tools in real time.

## What it does

Give it a GitHub username, and it returns:
- Name
- Bio
- Public repo count
- Followers / following
- Profile URL

## Tech stack

- Python 3.10+
- [MCP Python SDK](https://github.com/modelcontextprotocol)
- `requests` for calling the GitHub public API

## Setup

1. Clone this repo
2. Create a virtual environment:
