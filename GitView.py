import requests


def file_scan():
    try:
        input_file = input("File name : ")
        usernames = []
        with open(input_file, "r") as f:
            for users in f:
                if users.strip():
                    usernames.append(users.strip())
    except FileNotFoundError:
        print("File not found!")
        return
            
    for username in usernames:
        try: 

            url = f"https://api.github.com/users/{username}"
            response = requests.get(url, timeout=5)
                    

            response.raise_for_status()

                
            data = response.json()
            header = response.headers

            print(f"\n==== Info for {username} ====\n")
            print(f"{'Username':<15} : {data.get('login', 'Not available')}")
            print(f"{'Name':<15} : {data.get('name', 'Not available')}")
            print(f"{'Followers':<15} : {data.get('followers')}")
            print(f"{'Following':<15} : {data.get('following')}")
            print(f"{'Public Repos':<15} : {data.get('public_repos')}")
            print(f"{'Location':<15} : {data.get('location', 'Not available')}")
            print(f"{'Bio':<15} : {data.get('bio', 'Not available!')}")
            print(f"\n\n===== Headers =====")
                        
            for key, value in header.items():
                print(f"{key:<25} : {value}")

        except requests.exceptions.HTTPError as httper:
            status = httper.response.status_code if httper.response else 'Unknown'
            if status == 404:
                print(f"{username} not found (404)!")
            else:
                print(f"HTTP error for {username}: {httper}")


        except requests.exceptions.Timeout:
            print(f"Request timed out for {username}")

        except Exception as e:
            print("Error : ", e)


def specific_username():
    input_username = input("Enter username : ")
    try:
        url = f"https://api.github.com/users/{input_username}"

        
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        header = response.headers


        print(f"\n==== Info for {input_username} ====\n")
        print(f"{'Username':<15} : {data.get('login', 'Not available')}")
        print(f"{'Name':<15} : {data.get('name', 'Not available')}")
        print(f"{'Followers':<15} : {data.get('followers')}")
        print(f"{'Following':<15} : {data.get('following')}")
        print(f"{'Public Repos':<15} : {data.get('public_repos')}")
        print(f"{'Location':<15} : {data.get('location', 'Not available')}")
        print(f"{'Bio':<15} : {data.get('bio', 'Not available!')}")
        print(f"\n\n===== Headers =====")
        for key, value in header.items():
            print(f"{key:<25} : {value}")
        
    except requests.exceptions.HTTPError as httper:
        status = httper.response.status_code if httper.response else 'Unknown'
        if status == 404:
            print(f"{input_username} not found (404)!")
        else:
            print(f"HTTP error for {input_username}: {httper}")


    except requests.exceptions.Timeout:
        print(f"Request timed out for {input_username}")

    except Exception as e:
        print("Error : ", e)
        

def main():
    while True:
        print("\n===== GitHub User Search Tool =====")
        print("1. Search single username.")
        print("2. Search usernames from file.")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            specific_username()
        elif choice == "2":
            file_scan()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()

    