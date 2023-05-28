import requests

def get_repository_stats(owner, repo):
    # Make a GET request to the GitHub API to retrieve repository information
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant information from the API response
        full_name = data["full_name"]
        description = data["description"]
        stargazers_count = data["stargazers_count"]
        forks_count = data["forks_count"]
        open_issues_count = data["open_issues_count"]
        watchers_count = data["watchers_count"]
        primary_language = data["language"]
        last_update = data["updated_at"]
        
        # Display the repository information
        print(f"Repository: {full_name}")
        print(f"Description: {description}")
        print(f"Stargazers: {stargazers_count}")
        print(f"Forks: {forks_count}")
        print(f"Open Issues: {open_issues_count}")
        print(f"Watchers: {watchers_count}")
        print(f"Primary Language: {primary_language}")
        print(f"Last Update: {last_update}")
    else:
        print(f"Failed to retrieve repository information. Status Code: {response.status_code}")

def get_profile_info(username):
    # Make a GET request to the GitHub API to retrieve profile information
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant information from the API response
        name = data["name"]
        bio = data["bio"]
        followers_count = data["followers"]
        following_count = data["following"]
        public_repos_count = data["public_repos"]
        created_at = data["created_at"]
        
        # Display the profile information
        print(f"Username: {username}")
        print(f"Name: {name}")
        print(f"Bio: {bio}")
        print(f"Followers: {followers_count}")
        print(f"Following: {following_count}")
        print(f"Public Repositories: {public_repos_count}")
        print(f"Account Created At: {created_at}")
    else:
        print(f"Failed to retrieve profile information. Status Code: {response.status_code}")

def get_user_repos(username):
    # Make a GET request to the GitHub API to retrieve user's repositories
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Display the list of repositories
        print(f"Repositories of {username}:")
        for index, repo in enumerate(data, start=1):
            print(f"{index}. {repo['name']}")
        
        # Prompt the user to choose a repository
        repo_number = int(input("Enter the number corresponding to the repository: ")) - 1
        if 0 <= repo_number < len(data):
            chosen_repo = data[repo_number]
            get_repository_stats(chosen_repo["owner"]["login"], chosen_repo["name"])
        else:
            print("Invalid repository number.")
    else:
        print(f"Failed to retrieve user repositories. Status Code: {response.status_code}")

def get_user_organizations(username):
    # Make a GET request to the GitHub API to retrieve user's organizations
    url = f"https://api.github.com/users/{username}/orgs"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Display the list of organizations
        print(f"Organizations of {username}:")
        for org in data:
            print(org["login"])
    else:
        print(f"Failed to retrieve user organizations. Status Code: {response.status_code}")

# Prompt the user to select an option
print("Choose an option:")
print("1. Check Repository Information")
print("2. Check User Repositories")
print("3. Check Profile Information")
print("4. Check User's Organizations")

option = input("Enter your choice (1, 2, 3, or 4): ")

if option == "1":
    # Prompt the user for the repository owner and name
    owner = input("Enter the repository owner: ")
    repo = input("Enter the repository name: ")

    # Call the function to retrieve and display the repository information
    get_repository_stats(owner, repo)
elif option == "2":
    # Prompt the user for the GitHub username
    username = input("Enter the GitHub username: ")
    
    # Check if the user wants to list repositories
    check_repos = input(f"Do you want to check the repositories of {username}? (Y/N): ")
    if check_repos.lower() == "y":
        get_user_repos(username)
    else:
        print("Invalid option.")
elif option == "3":
    # Prompt the user for the GitHub username
    username = input("Enter the GitHub username: ")
    
    # Call the function to retrieve and display the profile information
    get_profile_info(username)
elif option == "4":
    # Prompt the user for the GitHub username
    username = input("Enter the GitHub username: ")
    
    # Call the function to retrieve and display the user's organizations
    get_user_organizations(username)
else:
    print("Invalid option. Please choose 1, 2, 3, or 4.")