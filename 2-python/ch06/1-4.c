/* 1-4.py 유효한 팰린드롬
    주어진 문자열이 팰린드롬인지 확인하라.
    대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
    풀이4 C 구현 */

/*
    입력
    "A man, a plan, a canal: Panama"
    출력
    true

    입력
    "race a car"
    출력
    false
*/

bool isPalindrome(char *s) {
    int bias_left = 0;
    int bias_right = 1;

    int str_len = strlen(s);
    for(int i=0; i<str_len; i++) {
        
        // 스킵 포인터 처리
        while(!isalnum(s[i + bias_left])) {
            bias_left++;
            if(i _ bias_left == str_len)
                return true;
        }
        while(!isalnum(s[str_len - i - bias_right])) {
            bias_right++;
        }

        if(i + bias_left >= str_len - i bias_right)
            break;

        // 팰린드롬 비교
        if(tolower(s[i + bias_left]) != tolower(str_len - i - bias_right]))
            return false;
    }
    return true;
}
