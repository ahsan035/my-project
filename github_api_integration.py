import requests
import base64
import time

# Replace 'YOUR_GITHUB_TOKEN' with your GitHub Personal Access Token
github_token = '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'

def search_python_repositories():
    headers = {
        'Authorization': f'token {github_token}'
    }
    params = {
        'q': 'language:python',
        'per_page': 10
    }
    response = requests.get('https://api.github.com/search/repositories', headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for repo in data['items']:
            print(f"Repository Name: {repo['name']}")
            print(f"URL: {repo['html_url']}")
            print("-----------------------------")
            # Call get_python_code_snippets() to retrieve code snippets for each repository
            get_python_code_snippets(repo['owner']['login'], repo['name'])
    else:
        print(f"Failed to retrieve repositories. Status code: {response.status_code}")
        print(f"Error message: {response.text}")

def get_python_code_snippets(owner, repo):
    headers = {
        'Authorization': f'token {github_token}'
    }
    url = f'https://api.github.com/repos/{owner}/{repo}/contents'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for file in data:
            if file['type'] == 'file' and file['name'].endswith('.py'):
                file_url = file['html_url']
                print(f"Python Code File: {file['name']}")
                print(f"URL: {file_url}")
                print("-----------------------------")
                # Get the content of the Python file with retries and delay
                for _ in range(3):  # Retry up to 3 times if request fails
                    try:
                        file_response = requests.get(file['download_url'], headers=headers)
                        file_response.raise_for_status()  # Check for any request errors
                        content = base64.b64decode(file_response.json()['content']).decode('utf-8')
                        # Here, you can parse the 'content' variable to extract code snippets.
                        # For example, you can use regular expressions to find code blocks or functions.
                        print(content)  # Print the content for demonstration purposes
                        break  # Break out of the retry loop if successful
                    except requests.exceptions.RequestException as e:
                        print(f"Failed to retrieve Python code file content: {file_url}. Error: {e}")
                        time.sleep(2)  # Add a delay of 2 seconds before retrying
                    except (KeyError, base64.binascii.Error) as e:
                        print(f"Failed to decode content for: {file_url}. Error: {e}")
                        break  # Break out of the retry loop if decoding fails
                    except ValueError as e:
                        print(f"Failed to parse JSON response for: {file_url}. Error: {e}")
                        break  # Break out of the retry loop if JSON parsing fails
    else:
        print(f"Failed to retrieve Python code files for repository: {owner}/{repo}. Status code: {response.status_code}")
        print(f"Error message: {response.text}")

if __name__ == "__main__":
    search_python_repositories()
