def eat_cookie(cookies: int) -> int:
    cookies = cookies - 1
    return cookies

def main() -> None:
    og_cookies = 3
    new_cookies = eat_cookie(og_cookies)
    print(og_cookies, new_cookies)

main()