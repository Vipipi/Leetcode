class Solution:
    thousands = ["","Thousand","Million","Billion"]
    less_than_20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
    "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen",
    "Eighteen","Nineteen"]
    tens = ["","Tens","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty",
    "Ninety","Hundred"]
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        i = 0
        ans = ""
        while num > 0:
            if num % 1000 != 0:
                ans = self.helper(num%1000) + self.thousands[i] +  " " + ans
            num //= 1000
            i += 1
        return ans.strip()

    def helper(self, n):
        if n == 0:
             return ""
        elif n < 20:
             return self.less_than_20[n] + " "
        elif n < 100:
             return self.tens[n//10] + " " + self.helper(n % 10)
        else:
             return self.less_than_20[n // 100] + " Hundred " + self.helper(n % 100)
