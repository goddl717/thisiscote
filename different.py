def solution(encrypted_text, key, rotation):
    answer = ''
    n = len(encrypted_text)
    rotation %= n
    encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]
    

    for idx in range(n):
        encrypted_alpha = ord(encrypted_text[idx]) - 96
        key_alpha = ord(key[idx]) - 96
        alpha_diff = (encrypted_alpha - key_alpha) % 26 if (encrypted_alpha - key_alpha) % 26 != 0 else 26
        answer += chr(alpha_diff + 96)

    return answer

print (solution("qyyigoptvfb",	"abcdefghijk"	,3))