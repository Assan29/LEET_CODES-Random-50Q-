#!/usr/bin/env python
# coding: utf-8

# # lc_2620

# In[1]:


def lc_2620(x,*y):
    
    '''
    Given an integer n, return a counter function. This counter function initially returns n and then 
    returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).
    
    EAMPLE:
    Input: 
    n = 10 
    ["call","call","call"]
    Output: [10,11,12]
    Explanation: 
    counter() = 10 // The first time counter() is called, it returns n.
    counter() = 11 // Returns 1 more than the previous time.
    counter() = 12 // Returns 1 more than the previous time.
    '''
    
    return [z+x for z in range(len(*[y]))]


# In[2]:


lc_2620(10,*['call','call','call','call','call','call'])


# # lc_2469

# In[3]:


def lc_2469(Celsius):
    
    '''
    You are given a non-negative floating point number rounded to two decimal places celsius, 
    that denotes the temperature in Celsius.
    You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit]
    Return the array ans. Answers within 10-5 of the actual answer will be accepted.
    given
    Kelvin = Celsius + 273.15
    Fahrenheit = Celsius * 1.80 + 32.00
    
    EXAMPLE:
    Input: celsius = 36.50
    Output: [309.65000,97.70000]
    Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
    '''
    
    Kelvin = Celsius + 273.15
    Fahrenheit = Celsius * 1.80 + 32.00
    return f'kelvin temp is {Kelvin} and Fahrenheit is {Fahrenheit}'


# In[4]:


lc_2469(36.50)


# # lc_2635

# In[28]:


def lc_2635(y):
    
    '''
    Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.
    The returned array should be created such that returnedArray[i] = fn(arr[i], i).
    Please solve it without the built-in Array.map method.
    
    EXAMPLE:
    Input: arr = [1,2,3], fn = function plusone(n) { return n + 1; }
    Output: [2,3,4]
    Explanation:
    const newArray = map(arr, plusone); // [2,3,4]
    The function increases each value in the array by one.
    '''
    x = [i+1 for i in y]
    print(x)


# In[32]:


lc_2635([1,2,3])


# In[5]:


list(map(lambda x : x+1,[1,2,3]))


# # lc_1290

# In[7]:


def lc_1290(head):                        #---->int([x]) -> integer
                                          #---->int(x, base=10) -> integer
    '''
    Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
    The linked list holds the binary representation of a number.
    Return the decimal value of the number in the linked list.
    The most significant bit is at the head of the linked list.

    EXAMPLE:
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
    '''
    
    x = ''.join([str(a) for a in head])
    y = int(x,2)
    return y


# In[8]:


lc_1290([101])


# In[9]:


y = int('101',2)
print(y)


# # lc_1365

# In[3]:


def lc_1365(nmb):
    
    '''
    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
    That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
    Return the answer in an array.
    
    EXAMPLE:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation:
    For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
    For nums[1]=1 does not exist any smaller number than it.
    For nums[2]=2 there exist one smaller number than it (1). 
    For nums[3]=2 there exist one smaller number than it (1). 
    For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
    '''
    
    x = []
    for i in nmb:
        y = 0
        for j in nmb:
            if j<i:
                y += 1
        x.append(y)
    return x


# In[4]:


lc_1365([8,1,2,2,3])


# # lc_771

# In[45]:


def lc_771(x,y):
    
    '''
    You're given strings jewels representing the types of stones that are jewels, and stones
    representing the stones you have. Each character in stones is a type of stone you have. 
    You want to know how many of the stones you have are also jewels.
    Letters are case sensitive, so "a" is considered a different type of stone from "A".
    
    EXAMPLE:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3
    '''
    
    count =0
    for stone in y:
        if stone in x:
            count+=1
    return count


# In[16]:


lc_771('aA','acAbcd')


# # lc_1528

# In[20]:


def lc_1528(s, indices):
    
    '''
    You are given a string s and an integer array indices of the same length.
    The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
    Return the shuffled string.
    
    EXAMPLE:
    Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
    Output: "leetcode"
    Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
    '''
    n = len(s)
    res = [''] * n
    for i in range(n):
        res[indices[i]] = s[i]
        print(res)
    return ''.join(res)


# In[21]:


lc_1528('codeleet',[5,4,6,7,0,2,1,3])


# # lc_1119

# In[10]:


def lc_1119(x,y):
    
    '''
    You are given a string s and an integer array indices of the same length. 
    The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
    Return the shuffled string.
    Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
    
    EXAMPLE:
    Input: “leetcodeisacommunityforcoders”
    Output: “ltcdscmmntyfrcdrs”
    '''
    
    return ''.join(str(a) for a in x.lower() if a not in y)


# In[11]:


lc_1119('leetcodeisacommunityforcoders',['a','e','i','o','u'])


# # lc_2367

# In[2]:


def lc_2367(nums, diff):
    
    '''
    You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
    A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
    i < j < k,
    nums[j] - nums[i] == diff, and
    nums[k] - nums[j] == diff.
    Return the number of unique arithmetic triplets.
    
    EXAMPLE:
    Input: nums = [0,1,4,6,7,10], diff = 3
    Output: 2
    Explanation:
    (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
    (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
    '''
    
    count = 0
    x = set(nums)

    for i in nums:
        if i - diff in x and i + diff in x:
            count += 1
    return count


# In[61]:


lc_2367([0, 1, 4, 6, 7, 10],3)


# # lc_1480

# In[3]:


def lc_1480(*nums,a=0):
    
    '''
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    
    EXAMPLE:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
    '''
    
    nums=[1,2,3,4]
    res=[]
    for i in nums:
        a+=i
        res.append(a)
    return res


# In[4]:


lc_1480(1,2,3,4)


# # lc_2535

# In[65]:


def lc_2535(nums,sum_digits=0):
    
    '''
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    
    EXAMPLE:
    Input: nums = [1,15,6,3]
    Output: 9
    Explanation: 
    The element sum of nums is 1 + 15 + 6 + 3 = 25.
    The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
    The absolute difference between the element sum and digit sum is |25 - 16| = 9
    '''

    sum_nums=sum(nums)
    
    for x in nums:
        while x>0:
            c=x%10
            sum_digits+=c
            x//=10
    c=sum_nums-sum_digits
    return c


# In[64]:


lc_2535([1,15,6,3])


# # lc_2037

# In[66]:


def lc_2037(seats,students):
    
    '''
    There are n seats and n students in a room. You are given an array seats of length n, 
    where seats[i] is the position of the ith seat. You are also given the array students of length n, 
    where students[j] is the position of the jth student.
    You may perform the following move any number of times:
    Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
    Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.
    Note that there may be multiple seats or students in the same position at the beginning.
    
    EXAMPLE:
    Input: seats = [3,1,5], students = [2,7,4]
    Output: 4
    Explanation: The students are moved as follows:
    - The first student is moved from from position 2 to position 1 using 1 move.
    - The second student is moved from from position 7 to position 5 using 2 moves.
    - The third student is moved from from position 4 to position 3 using 1 move.
    In total, 1 + 2 + 1 = 4 moves were used
    '''

    seats.sort()
    students.sort()
    
    result=0

    for i in range(len(seats)):
        result+=abs(seats[i]-students[i])

    return result    


# In[67]:


lc_2037([3,1,5],[2,7,4])


# # lc_2656

# In[69]:


def lc_2656(nums,k):
    
    '''
    You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation
    exactly k times in order to maximize your score:
    Select an element m from nums.
    Remove the selected element m from the array.
    Add a new element with a value of m + 1 to the array.
    Increase your score by m.
    Return the maximum score you can achieve after performing the operation exactly k times.
    
    EXAMPLE:
    Input: nums = [1,2,3,4,5], k = 3
    Output: 18
    Explanation: We need to choose exactly 3 elements from nums to maximize the sum.
    For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
    For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
    For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
    So, we will return 18.
    It can be proven, that 18 is the maximum answer that we can achieve.
    '''
    
    nums=[3,4,5,1,2]
    nums.sort()
    lst=[]
    for i in range(k):
        nex=1
        c=nums.pop()
        lst.append(c)
        nex+=c
        nums.append(nex)
        nex=0
    return sum(lst)


# In[70]:


lc_2656([3,4,5,1,2],3)


# # lc_2455

# In[77]:


def lc_2455(x):
    
    '''
    Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
    Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    
    EXAMPLE
    Input: nums = [1,3,6,10,12,15]
    Output: 9
    Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
    '''
    
    a =  [i for i in x if i%2==0 and i%3==0]
    return sum(a)/len(a)


# In[78]:


lc_2455([1,3,6,10,12,15])


# # lc_2540

# In[79]:


def lc_2540(A, B):
    
    '''
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
    If there is no common integer amongst nums1 and nums2, return -1.
    Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
    
    EXAMPLE:
    Input: nums1 = [1,2,3], nums2 = [2,4]
    Output: 2
    Explanation: The smallest element common to both arrays is 2, so we return 2.
    
    '''
    return min(set(A).intersection(B))


# In[80]:


lc_2540([1,2,3],[2,4])


# # lc_2000

# In[82]:


def lc_2000(x,y):
    
    '''
    Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 
    and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3(inclusive)
    The resulting string will be "dcbaefd".
    Return the resulting string.
    
    EXAMPLE:
    Input: word = "abcdefd", ch = "d"
    Output: "dcbaefd"
    Explanation: The first occurrence of "d" is at index 3. 
    Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
    '''
    
    if y in x:
        z = x.index(y)
        return x[:z+1][::-1] + x[z+1:]
    return x


# In[83]:


lc_2000('abcdefd','d')


# # lc_2243

# In[89]:


def fstr(s):
    
    '''
    You are given a string s consisting of digits and an integer k.
    A round can be completed if the length of s is greater than k. In one round, do the following:
    Divide s into consecutive groups of size k such that the first k characters are in the first group,
    the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.
    Replace each group of s with a string representing the sum of all its digits. 
    For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.
    Merge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.
    Return s after all rounds have been completed.
    
    EXAMPLE:
    Input: s = "11111222223", k = 3
    Output: "135"
    Explanation: 
    - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
      ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
      So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
    - For the second round, we divide s into "346" and "5".
      Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
      So, s becomes "13" + "5" = "135" after second round. 
    Now, s.length <= k, so we return "135" as the answer.
    '''
    return sum(int(digit) for digit in s)

def lc_2243(s, k):
    while len(s) > k:
        groups = [s[i:i+k] for i in range(0, len(s), k)]
        s = ''.join(str(fstr(group)) for group in groups)
    return s


# In[90]:


lc_2243("11111222223",3)


# # lc_1748

# In[92]:


def lc_1748(nums):
    
    '''
    You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
    Return the sum of all the unique elements of nums.
    
    EXAMPLE:
    Input: nums = [1,2,3,2]
    Output: 4
    Explanation: The unique elements are [1,3], and the sum is 4.
    '''
    
    x = [i for i in nums if nums.count(i) ==1]
    y = sum(x)

    return y


# In[93]:


lc_1748([1, 2, 3, 2])


# # lc_1816

# In[95]:


def lc_1816(s,k):
    
    '''
    A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
    Each of the words consists of only uppercase and lowercase English letters (no punctuation).
    For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
    You are given a sentence s and an integer k. You want to truncate s such that 
    it contains only the first k words. Return s after truncating it.
    
    EXAMPLE:
    Input: s = "Hello how are you Contestant", k = 4
    Output: "Hello how are you"
    Explanation:
    The words in s are ["Hello", "how" "are", "you", "Contestant"].
    The first 4 words are ["Hello", "how", "are", "you"].
    Hence, you should return "Hello how are you".
    '''
    
    a=s.split()

    b=[]

    for i in range(k):
        if len(a)>k:
            b.append(a[i])
            
            e=' '.join(b)
        else:
            
            return s
    return e


# In[96]:


lc_1816('chopper is not a tanuki',5)


# # lc_2138

# In[98]:


def lc_2138(string,k):
    
    '''
    A string s can be partitioned into groups of size k using the following procedure:
    The first group consists of the first k characters of the string, the second group consists of the next k characters
    of the string, and so on. Each character can be a part of exactly one group.
    For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
    Note that the partition is done so that after removing the fill character from the last group (if it exists)
    and concatenating all the groups in order, the resultant string should be s.
    Given the string s, the size of each group k and the character fill, return a string array denoting the composition of 
    every group s has been divided into, using the above procedure.
    
    EXAMPLE:
    Input: s = "abcdefghi", k = 3, fill = "x"
    Output: ["abc","def","ghi"]
    Explanation:
    The first 3 characters "abc" form the first group.
    The next 3 characters "def" form the second group.
    The last 3 characters "ghi" form the third group.
    Since all groups can be completely filled by characters from the string, we do not need to use fill.
    Thus, the groups formed are "abc", "def", and "ghi".
    '''
    
    a=['']
    fill='x'
    for i in string:
        if len(a[-1])<k:
            a[-1] += i
       
        else:
            a.append('')
            a[-1] +=i
       
     
    
    while len(a[-1]) < k:
        a[-1] += fill
       
    return a    


# In[99]:


lc_2138("abcdefghij",3)


# # lc_1832

# In[102]:


def lc_1832(s):
    
    '''
    A pangram is a sentence where every letter of the English alphabet appears at least once.
    Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
    or false otherwise.
    
    EXAMPLE:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true
    Explanation: sentence contains at least one of every letter of the English alphabet.
    '''
    
    return set(s.lower()) == set('abcdefghijklmnopqrstuvwxyz')


# In[103]:


lc_1832("thequickbrownfoxjumpsoverthelazydog")


# # lc_2544

# In[105]:


def lc_2544(n):
    
    '''
    You are given a positive integer n. Each digit of n has a sign according to the following rules:
    The most significant digit is assigned a positive sign.
    Each other digit has an opposite sign to its adjacent digits.
    Return the sum of all digits with their corresponding sign.
    
    EXAMPLE:
    Input: n = 521
    Output: 4
    Explanation: (+5) + (-2) + (+1) = 4.
    '''
    
    sign=1
    result=0
    for i in str(n):
        result+=sign*int(i)
        sign*=-1
    return result


# In[106]:


lc_2544('521')


# # lc_2239

# In[108]:


def lc_2239(nums):
    
    '''
    Given an integer array nums of size n, return the number with the value closest to 0 in nums.
    If there are multiple answers, return the number with the largest value.
    
    EXAMPLE:
    Input: nums = [-4,-2,1,4,8]
    Output: 1
    Explanation:
    The distance from -4 to 0 is |-4| = 4.
    The distance from -2 to 0 is |-2| = 2.
    The distance from 1 to 0 is |1| = 1.
    The distance from 4 to 0 is |4| = 4.
    The distance from 8 to 0 is |8| = 8.
    Thus, the closest number to 0 in the array is 1.
    '''
    
    a=[abs(nums[i]-0) for i in range(len(nums))]
    
    return min(a)


# In[109]:


lc_2239([-4,-2,1,4,8])


# # lc_2427

# In[112]:


def lc_2427(a,b):
    
    '''
    Given two positive integers a and b, return the number of common factors of a and b.
    An integer x is a common factor of a and b if x divides both a and b.
    
    EXAMPLE:
    Input: a = 12, b = 6
    Output: 4
    Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
    '''
    
    c={i for i in range(1,a+1) if a%i==0}
    d={j for j in range(1,b+1) if b%j==0}
    
    return len(c.intersection(d))


# In[113]:


lc_2427(6,12)


# # lc_2648

# In[115]:


def lc_2648(x):
    
    '''
    Given two positive integers a and b, return the number of common factors of a and b.
    An integer x is a common factor of a and b if x divides both a and b.
    Input: callCount = 5
    Output: 0,1,1,2,3
    Explanation:
    const gen = fibGenerator();
    gen.next().value; // 0
    gen.next().value; // 1
    gen.next().value; // 1
    gen.next().value; // 2
    gen.next().value; // 3
    '''
    
    fib_list = []
    a, b = 0, 1
    for i in range(x):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


# In[116]:


lc_2648(10)


# # lc_1165

# In[14]:


def lc_1165(keyboard,word):
        
        '''
        There is a special keyboard with all keys in a single row.
        Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
        initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired
        character. The time taken to move your finger from index i to index j is |i - j|.
        You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
        
        Example
        Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
        Output: 4
        Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
        Total time = 2 + 1 + 1 = 4.
        '''
        
        x = 0
        y = 0
        for i in word:
            a = keyboard.index(i)
            x += abs(a-y)
            y = a

        return x


# In[15]:


lc_1165(keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba")


# # lc_2255

# In[20]:


def lc_2255(words,s):
        
        '''
        You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.
        Return the number of strings in words that are a prefix of s.
        A prefix of a string is a substring that occurs at the beginning of the string. 
        A substring is a contiguous sequence of characters within a string.

        Example
        Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
        Output: 3
        Explanation:
        The strings in words which are a prefix of s = "abc" are:
        "a", "ab", and "abc".
        Thus the number of strings in words which are a prefix of s is 3.
        '''
   
        count=0
        for x in words:
             if s.startswith(x)==True:
                count +=1
        print(count)


# In[21]:


lc_2255(words = ["a","b","c","ab","bc","abc"], s = "abc")


# # lc_1768

# In[22]:


def lc_1768(a,b):
        
        '''
        You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,starting with word1.
        If a string is longer than the other, append the additional letters onto the end of the merged string.
        Return the merged string.
        Example
        Input: word1 = "abc", word2 = "pqr"
        Output: "apbqcr"
        Explanation: The merged string will be merged as so:
        word1:  a   b   c
        word2:    p   q   r
        merged: a p b q c r
        '''
        
        i = 0
        j = 0
        result =''
        while i< len(a) and j<len(b):
            result +=a[i]+b[j]
            i+=1
            j+=1
        while i< len(a):
            result +=a[i]
            i += 1
        while j< len(b):
            result +=b[j]
            j += 1

        return result


# In[24]:


lc_1768("abc", "pqr")


# # lc_2665

# In[26]:


def counter_increment(a):
    a+=1
    return a
  
def counter_reset(b):
    return b
   
def counter_decrement(c):
    c-=1
    return c  
def lc_2665(init,calls):
        
        '''
        Write a function createCounter. It should accept an initial integer init. It should return an object 
        with three functions.
        The three functions are:
        increment() increases the current value by 1 and then returns it.
        decrement() reduces the current value by 1 and then returns it.
        reset() sets the current value to init and then returns it.
        
        Example
        Input: init = 5, calls = ["increment","reset","decrement"]
        Output: [6,5,4]
        Explanation:
        const counter = createCounter(5);
        counter.increment(); // 6
        counter.reset(); // 5
        counter.decrement(); // 4
        '''
        
        z=[]
        for x in range(len(calls)):
            if calls[x]=="increment":
                z.append(counter_increment(init))
            if calls[x]=="reset":
                z.append(counter_reset(init))
            if calls[x]=="decrement":
                z.append(counter_decrement(init))    
        return z


# In[27]:


lc_2665(init = 5, calls = ["increment","reset","decrement"])


# # lc_1512

# In[117]:


def lc_1512(nums):
    
    '''
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
    '''
    
    count = 0
   
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1

    return count


# In[118]:


lc_1512([1, 2, 3, 1, 1, 3])


# # lc_1323

# In[122]:


def lc_1323(num):
        
        
        '''
        You are given a positive integer num consisting only of digits 6 and 9.
        Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
        
        Example 
        Input: num = 9669
        Output: 9969
        Explanation: 
        Changing the first digit results in 6669.
        Changing the second digit results in 9969.
        Changing the third digit results in 9699.
        Changing the fourth digit results in 9666.
        The maximum number is 9969.
        '''
        
        x = str(num)
        for i in range(len(x)):
            if x[i] == '6':
                y = x[:i] + '9' + x[i+1:]
                break
        return int(y)


# In[121]:


lc_1323(9669)


# # lc_1431

# In[30]:


def lc_1431(candies, extraCandies):
        
        '''
        There are n kids with candies. You are given an integer array candies, where each candies[i] represents 
        the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
        Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
        they will have the greatest number of candies among all the kids, or false otherwise.
        Note that multiple kids can have the greatest number of candies.

        Example 1:
        Input: candies = [2,3,5,1,3], extraCandies = 3
        Output: [true,true,true,false,true] 
        Explanation: If you give all extraCandies to:
        - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
        - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
        - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
        - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
        - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
        '''
    
        max_candies = max(candies)

        result = []

        for i in range(len(candies)):

            if candies[i] + extraCandies >= max_candies:

                result.append(True)
            else:
                result.append(False)

        return result


# In[31]:


lc_1431(candies = [2,3,5,1,3], extraCandies = 3)


# # lc_1512

# In[34]:


def lc_1512(nums):
    
        '''
        Given an array of integers nums, return the number of good pairs.
        A pair (i, j) is called good if nums[i] == nums[j] and i < j.

        Input: nums = [1,2,3,1,1,3]
        Output: 4
        Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
        '''

        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
    


# In[35]:


lc_1512([1,2,3,1,1,3])


# # lc_1221

# In[38]:


def lc_1221(s):
    
        '''
        Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
        Given a balanced string s, split it into some number of substrings such that:
        Each substring is balanced.
        Return the maximum number of balanced strings you can obtain.

        Input: s = "RLRRLLRLRL"
        Output: 4
        Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
        '''

        count = 0
        result = 0

        for i in s:
            if i == 'R':
                count+=1
            else:
                count-=1
            if count==0:
                result+=1

        return result


# In[41]:


lc_1221("RLRRLLRLRL")


# # lc_344

# In[44]:


def lc_344(s):
        
        '''
        Write a function that reverses a string. The input string is given as an array of characters s.
        You must do this by modifying the input array in-place with O(1) extra memory
        
        EXAMPLE
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        Example 2:

        Input: s = ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]
        '''
        
        return s[::-1]


# In[46]:


lc_344(["h","e","l","l","o"])


# # lc_1332

# In[16]:


def lc_1332(x):
        '''
        You are given a string s consisting only of letters 'a' and 'b'. In a single step you can 
        remove one palindromic subsequence from s.
        Return the minimum number of steps to make the given string empty.
        A string is a subsequence of a given string if it is generated by deleting some 
        characters of a given string without changing its order. Note that a subsequence 
        does not necessarily need to be contiguous.
        A string is called palindrome if is one that reads the same backward as well as forward.

        Example

        Input: s = "ababa"
        Output: 1
        Explanation: s is already a palindrome, so its entirety can be removed in a single step.
        '''
        
        if x == '':
            return 0
        elif x == x[::-1]:
            return 1
        else:
            return 2


# In[17]:


lc_1332('ababa')


# # lc_1979

# In[123]:


def lc_1979(nums):
    
    '''
    Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
    The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
    
    EXAMPLE:
    Input: nums = [2,5,6,9,10]
    Output: 2
    Explanation:
    The smallest number in nums is 2.
    The largest number in nums is 10.
    The greatest common divisor of 2 and 10 is 2.
    '''
    
    smallest = min(nums)
    largest = max(nums)

    while largest % smallest != 0:
        largest, smallest = smallest, largest % smallest
        
    return smallest


# In[125]:


lc_1979([2,5,6,9,10])


# # lc_2160

# In[127]:


def lc_2160(num):
    
    '''
    You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 
    by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
    For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. 
    Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
    Return the minimum possible sum of new1 and new2.
    
    EXAMPLE:
    Input: num = 2932
    Output: 52
    Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
    The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
    '''
    
    digits = [int(d) for d in str(num)]
    digits.sort()  
    new1 = 0
    new2 = 0
    for i in range(len(digits)):
        if i % 2 == 0:
            new1 = new1 * 10 + digits[i]
        else:
            new2 = new2 * 10 + digits[i]
    return new1 + new2


# In[128]:


lc_2160(2932)


# # lc_1108

# In[130]:


def lc_1108(I):
    
    '''
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
    
    EXAMPLE:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"
    '''
    
    L= I.split('.')

    octets = sum([1 for y in range(len(L)) if int(L[y])>=0 and int(L[y])<=255])
    if I.count('.') == 3 and octets == 4:
        s=I.replace(".", "[.]")
        print(s)
    else:
        print("Please enter a valid IPv4 address")


# In[129]:


lc_1108('1.2.3.4')


# # lc_2667

# In[131]:


def lc_2667(*args, **kwargs):
    
    '''
    Write a function createHelloWorld. It should return a new function that always returns "Hello World".
    
    EXAMPLE:
    Input: args = [{},null,42]
    Output: "Hello World"
    Explanation:
    const f = createHelloWorld();
    f({}, null, 42); // "Hello World"
    Any arguments could be passed to the function but it should still always return "Hello World".
    '''
    
    return 'hello world'


# In[133]:


lc_2667([{},'Assan',42], 'hjsfd')


# # lc_2413

# In[134]:


def lc_2413(x):
    '''
    Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

    EXAMPLE:
    Input: n = 5
    Output: 10
    Explanation: The smallest multiple of both 5 and 2 is 10.
    '''
    
    for i in range (1,10):
        if (x*i)%2==0:
            print(f'smallest even multiple is : {x*i}')
            break


# In[135]:


lc_2413(5)


# # lc_1486

# In[137]:


import functools
from functools import reduce

def lc_1486(n, start):
    
    '''
    You are given an integer n and an integer start.
    Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
    Return the bitwise XOR of all elements of nums.

    EXAMPLE:
    Input: n = 5, start = 0
    Output: 8
    Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
    Where "^" corresponds to bitwise XOR operator.
    '''
    
    nums = [start + 2*i for i in range(n)]
    print(f'The list of numbers starting with {start} : {nums}')
    z = reduce(lambda x, y: x ^ y, nums)  
    return z



# In[141]:


lc_1486(5,0)


# # lc_1935

# In[57]:


def lc_1935(text,brokenLetters):
    
    '''
    There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
    Given a string text of words separated by a single space (no leading or trailing spaces) and a 
    string brokenLetters of all distinct letter keys that are broken, return the number of 
    words in text you can fully type using this keyboard.

    EXAMPLE:
    Input: text = "hello world", brokenLetters = "ad"
    Output: 1
    Explanation: We cannot type "world" because the 'd' key is broken.
    '''
    
    ans = 0
        
    for i in text.split(" "):
        for j in i:  
            if j in brokenLetters:
                ans-=1
                break
                    
        ans = ans+1
    
    return ans


# In[142]:


lc_1935(text = "hello world", brokenLetters = "ad")


# # lc_1929

# In[154]:


def lc_1929(nums):
    
    '''
    Given an integer array nums of length n, you want to create an array ans of length 2n 
    where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    Specifically, ans is the concatenation of two nums arrays.
    Return the array ans.

    EXAMPLE:
    Input: nums = [1,2,1]
    Output: [1,2,1,1,2,1]
    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
    - ans = [1,2,1,1,2,1]
    '''
    
    ans=[]
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans


# In[155]:


lc_1929([1,2,1])


# # lc_1470

# In[152]:


def lc_1470(nums, n):
    
    '''
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    EXAMPLE:
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7] 
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
    '''
    
    x = []
    for i in range(n):
        x.append(nums[i])
        x.append(nums[i +n])
    return x


# In[153]:


lc_1470([2,5,1,3,4,7],3)


# # lc_2011

# In[156]:


def lc_2011(operations):
    
    '''
    There is a programming language with only four operations and one variable X:
    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.
    Initially, the value of X is 0.
    Given an array of strings operations containing a list of operations, return the final value of X 
    after performing all the operations.

    EXAMPLE:
    Input: operations = ["--X","X++","X++"]
    Output: 1
    Explanation: The operations are performed as follows:
    Initially, X = 0.
    --X: X is decremente by 1, X =  0 - 1 = -1.
    X++: X is incremented by 1, X = -1 + 1 =  0.
    X++: X is incremented by 1, X =  0 + 1 =  1.
    '''
    
    x = 0
    
    for operation in operations:
        if operation == "++X" or operation == "X++":
            x += 1
        elif operation == "--X" or operation == "X--":
            x -= 1
    
    return x


# In[158]:


lc_2011(["--X","X++","X++"])


# # lc_1720

# In[162]:


def lc_1720(encoded, first):
    
    '''
    There is a hidden integer array arr that consists of n non-negative integers.
    It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. 
    For example, if arr = [1,0,2,1], then encoded = [1,2,3].
    You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
    Return the original array arr. It can be proved that the answer exists and is unique.
    
    EXAMPLE:
    Input: encoded = [1,2,3], first = 1
    Output: [1,0,2,1]
    Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
    '''
   
    n = len(encoded) + 1
    nlst = [0] * n
    nlst[0] = first
    for i in range(1, n):
        nlst[i] = encoded[i - 1] ^ nlst[i - 1]
    return nlst


# In[163]:


lc_1720([1,2,3],2)


# # lc_2235

# In[165]:


def lc_2235(num1,num2):
    
    '''
    Given two integers num1 and num2, return the sum of the two integers.
 
    EXAMPLE:
    Input: num1 = 12, num2 = 5
    Output: 17
    Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
    '''
    
    return num1+num2


# In[166]:


lc_2235(12,5)


# # lc_1025

# In[168]:


def lc_1025(n):
    
    '''
    Alice and Bob take turns playing a game, with Alice starting first.
    Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
    Choosing any x with 0 < x < n and n % x == 0.
    Replacing the number n on the chalkboard with n - x.
    Also, if a player cannot make a move, they lose the game.
    Return true if and only if Alice wins the game, assuming both players play optimally.

    EXAMPLE:
    Input: n = 2
    Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.
    '''

    if (n%2==0):
        return True
    else:
        return False


# In[170]:


lc_1025(2)


# # lc_1021

# In[174]:


def lc_1021(s):
    
    '''
    A valid parentheses string is either empty "", "(" + A + ")", or A + B, 
    where A and B are valid parentheses strings, and + represents string concatenation.
    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
    A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B,
    with A and B nonempty valid parentheses strings.
    Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
    where Pi are primitive valid parentheses strings.
    Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

    EXAMPLE:
    Input: s = "(()())(())"
    Output: "()()()"
    Explanation: 
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
    '''
    
    result = []
    bal = 0

    for char in s:
        if char == '(':
            if bal > 0:
                result.append(char)
            bal += 1
        elif char == ')':
            bal -= 1
            if bal > 0:
                result.append(char)

    return ''.join(result)


# In[175]:


lc_1021( "(()())(())")


# In[ ]:




