import urllib.request
import json
def get_popular_repos():
    url = "https://api.github.com/search/repositories?q=stars:>1&sort=stars&order=desc"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        repo_data = json.loads(data)
    return repo_data['items']
def get_repo_info(repo_id):
    url = f"https://api.github.com/repositories/{repo_id}"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        repo_info = json.loads(data)
    return repo_info
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
def main():
    repos = get_popular_repos()
    if len(repos) > 6:
        repo_info = get_repo_info(repos[6]['id'])
        data_to_save = {
            'company': repo_info.get('organization', {}).get('login', None),
            'created_at': repo_info.get('created_at'),
            'email': repo_info.get('organization', {}).get('email', None),
            'id': repo_info.get('id'),
            'name': repo_info.get('name'),
            'url': repo_info.get('html_url')
        }
        save_to_json(data_to_save, 'repo_info.json')
        print("Информация сохранена в файл repo_info.json")
    else:
        print("Не найдено достаточное количество репозиториев.")
if __name__ == "__main__":
    main()