# Programming Assignment: Pluto's Poetic Journey 🚀 

🧑‍🚀 In this exciting adventure, you'll be diving into the fascinating world of space exploration and poetry (yes, you read that right, poetry! 🖋️). You'll be using Python to analyze a captivating news article about the New Horizons spacecraft's journey to Pluto and its discoveries. Get ready to flex your coding muscles and unleash your inner poet! 💫

## The Assignment Briefing 📰

Your task begins with a [news article](https://edition.cnn.com/2020/07/15/world/pluto-new-horizons-anniversary-scn-trnd/index.html) detailing the incredible findings from the New Horizons mission. The spacecraft has sent back a treasure trove of information about the dwarf planet Pluto, revealing its secrets and captivating our imaginations. However, the article is quite long, and you need a more efficient way to understand its key themes.

## Table of Exercises

- [Exercise 1: Encountering Data - Reading the News Article 🛰️](#1)
- [Exercise 2: Decoding the Cosmos - Extracting Key Topics 🔭](#2)
- [Exercise 3: The Poet's Palette - Organizing Your Topics 🎨](#3)
- [Exercise 4: Cosmic Sonnets - Writing Your Space Poem 🖋️](#4)
- [Exercise 5: Preserving the Verse - Saving Your Poem 💾](#5)

### Assignment Starts From Here

Before starting the assignment, run the cell below. It will bring in some helpful code to check if your solutions are correct and provide feedback if you need to make changes.

**IMPORTANT NOTE**:  Always run this cell when starting or resuming your assignment. **DO NOT include it in any other notebook cells.**
     
The below cell also loads the helper functions you'll be needing in this assignment. 


```python
import test_your_code
from helper_functions import get_llm_response, print_formatted_list, print_formatted_list_of_dict, download_file
```

<a name='1'></a>
## Exercise 1: Encountering Data - Reading the News Article 🛰️

First things first, you need to access the news article. It's like receiving a transmission from a faraway probe - you need to decode it first. 

**Your Task:**

* Define a Python function called `read_article` that takes a `text_file` (string) as a parameter and reads the contents of the file. The function should return the contents of the file.

<span style="color: blue;">**Hint**</span>: You can refer to the classroom lesson *Turning code blocks into reusable functions* for this.


```python
# Define a Python function "read_article" and pass "text_file" as parameter
def read_article(text_file):
    
    ### START CODE HERE ###
    
    # "Open" "text_file" in "read" mode
    f = # Add your code here
    
    # Use "f.read()" to read the file into "contents"
    contents = # Add your code here
    
    # Close the file "f.close()"
    # Add your code here
    
    # Return "contents"
    return # Add your return variable here
    
    ### END CODE HERE ###
```


```python
# Test your code!
test_your_code.exercise_1(read_article)
```

**Important Note:** If you see <span style="color: green;">All tests passed!</span>, you can proceed to the next step. If there's an error message <span style="color: red;">in red</span>, follow the instructions to fix it, then re-run the exercise and test cells until you get the <span style="color: green;">All tests passed!</span> message. Repeat this process for all exercises in the assignment.

<a name='2'></a>
## Exercise 2: Decoding the Cosmos - Extracting Key Topics 🔭

Great work, your `read_article` function is working like a charm! Use it to receive your transmission:

You'll be using the news article [5 years after its Pluto flyby, New Horizons spacecraft forges ahead](https://edition.cnn.com/2020/07/15/world/pluto-new-horizons-anniversary-scn-trnd/index.html), published on July 15, 2020, written by CNN. This article has been saved in a `news_article.txt` file in your workspace.

Print the contents of this news article.


```python
news_article = read_article("news_article.txt")
print(news_article)
```

That is a lengthy article! To decipher its secrets without reading every word, employ a powerful tool: a Large Language Model (LLM). Think of it as your trusty AI assistant, capable of understanding and summarizing vast amounts of information. 🧠

You'll ask the LLM to analyze the news article and extract three key topics discussed.


```python
prompt = f"""
Read the contents of file {news_article}, and extract the key topics discussed in it. Provide exactly 3 key topics.
Each topic should not be more than 8 words.

Provide each topic in a new line.

Output Format:
topic_1

topic_2

topic_3

"""

response = get_llm_response(prompt)
```


```python
# Print the response
print(response)
```

**Your Task:**

Turn these topics into a single Python list.
* Copy/paste the topics generated from `response` above into the `key_topics` list below.

Be sure that:
* Each topic is stored as a "string"
* There are no duplicate topics in your list
* Don't forget to use a comma `,` after each entry in the list. For example:

```python
	key_topics = [
		"Topic 1",
		"Topic 2",
		"Topic 3"
	]
```


```python
key_topics = [
    
    ### START CODE HERE ###
    
    "Copy/Paste your first topic as a string in here",
    
    "Copy/Paste your second topic as a string in here",
    
    "Copy/Paste your third topic as a string in here"
    
    ### END CODE HERE ###

]

print_formatted_list(key_topics)
```

#### Expected Output:
```
[
    "Unique Topic 1 as a string",
    "Unique Topic 2 as a string",
    "Unique Topic 3 as a string"
]
```


```python
# Test your code!    
test_your_code.exercise_2(key_topics)    
```

<a name='3'></a>
## Exercise 3: The Poet's Palette - Organizing Your Topics 🎨 

Excellent work, your `key_topics` list is ready for action! Now, imagine you want to write a poem inspired by these topics, but you're not particularly fond of one or more of them.

To give you more control over your creative process, you'll be crafting a list of dictionaries, with each dictionary representing a topic and a special "switch" called `to_use`. This "switch" will tell the LLM whether or not to include a particular topic in the poem. It's like having a poet's palette, carefully selecting the colors and themes you want to use in your masterpiece! 🎨

**Your Task:**

Create a list of dictionaries `topics_to_use` with each topic from the list `key_topics` and a switch `to_use`. 

In each dictionary:
* Use the list `key_topics` to get the topic and add them into the new dictionary.
* Add a boolean value `to_use` (True would mean to use it in the Poem, False would mean not to use). Feel free to put True/False as you desire.

Be sure that:
* There are no duplicate topics in your list
* Don't forget to use a comma `,` after each entry in the dictionary and after each dictionary. For example:
```python
	{
		"Topic 1": your topic,
		
		"to_use": a boolean value
	},
	{
		"Topic 2": your topic,
		
		"to_use": a boolean value
	}
```


```python
topics_to_use = [
    
    ### START CODE HERE ###
    
    {
        # Use your the "first" entry from "key_topics" as "Topic 1"
        # Hint: Remember, in Python, counting starts from zero (0)
        "Topic 1": # First element from the list "key_topics" goes here,
        
        # Use a boolean value (True or False) for "to_use"
        "to_use": # Add boolean value here
    },
    {
        # Use your the "second" entry from "key_topics" as "Topic 2"
        "Topic 2": # Second element from the list "key_topics" goes here,
        
        # Use a boolean value (True or False) for "to_use"
        "to_use": # Add boolean value here
    },
    {
        # Use your the "third" entry from "key_topics" as "Topic 3"
        "Topic 3": # Third element from the list "key_topics" goes here,
        
        # Use a boolean value (True or False) for "to_use"
        "to_use": # Add boolean value here
    }
    
    ### END CODE HERE ###
    
]
    
print_formatted_list_of_dict(topics_to_use)
```

#### Expected Output:
```
[
    {
        "Topic 1": "Unique Topic 1 as a string",
        "to_use": A boolean value,
    },
    {
        "Topic 2": "Unique Topic 2 as a string",
        "to_use": A boolean value,
    },
    {
        "Topic 3": "Unique Topic 3 as a string",
        "to_use": A boolean value,
    }
]
```


```python
# Test your code!
test_your_code.exercise_3(topics_to_use, key_topics)
```

<a name='4'></a>
## Exercise 4: Cosmic Sonnets - Writing Your Space Poem 🖋️

With your `topics_to_use` list ready, it's time to enlist the LLM once again, this time for a more creative task: crafting your space poem! 🌠

**Your Task:**

Write a `prompt` that asks the LLM to generate a `poem`. The `poem` should be of exactly `4 (four)` `lines (line)`. Your `prompt` should also include the `topics_to_use` list.

    You have the flexibility to structure your prompt and wording as you see fit. The key is to include all three pieces of information (`topics_to_use` list, mention of writing a "poem" and using only "4 (four) lines (line)") naturally within the `prompt`'s instructions. 

    For example, your prompt could look something like this: 
    "Using only the topics from the list <topics_to_use>, write a 4-line poem."


```python
### START CODE HERE ###

prompt = f"""
# Add your code here
"""

### END CODE HERE ###

print(prompt)
```

#### Expected Output:
```
Your prompt containing the following details:
- `topics_to_use` list
- Instructions of writing a "poem"
- Using only "4 (four) lines (line)"
```

**Note:** You will fail the below test if your prompt excludes any one of the above mentioned details.


```python
# Test your code!    
test_your_code.exercise_4(prompt, topics_to_use)    
```


```python
poem = get_llm_response(prompt)
```


```python
# Print your poem
print(poem)
```

<a name='5'></a>
## Exercise 5: Preserving the Verse - Saving Your Poem 💾 

Your poem is a masterpiece! But like a fading transmission, it won't last forever unless you store it properly.

**Your Task:**

* Create a Python function called `save_to_file` that uses the parameter `contents_to_save` (a string) and saves it in a file called `poem.txt`.

<span style="color: blue;">**Hint**</span>: You can refer to the classroom lesson *Extracting restaurant information from journal entries* for this.


```python
# Define a Python function "save_to_file" and pass "contents_to_save" as parameter
def save_to_file(contents_to_save):
    
    ### START CODE HERE ###
    
    # Using "Open", open or create a text file `poem.txt` in "write" mode
    f = open("poem.txt", '# Add your code here')
    
    ### END CODE HERE ###
    
    # Write "contents_to_save" in the file `poem.txt`
    f.write(contents_to_save)
    
    # Close the file
    f.close()
```


```python
# Test your code!    
test_your_code.exercise_5(save_to_file) 
```

### Submission Note:
If you have passed all the tests up to this point, you can submit your assignment for grading.

**But before you submit your assignment, re-run the assignment just in case there are any unexpected errors present in the notebook once it goes for grading.** To do so, follow these steps:

1. Restart the `Kernel` and select the `Restart & Clear Output` option. You can do this by clicking on the `Kernel` menu at the top of the notebook.
![Kernel Restart Image](kernel_restart.png)
2. Once the kernel restarts and all outputs are clear, run the cells from top to bottom again up to this point.

If you have followed these steps and still pass all of the tests, you can submit your assignment for grading. If you encounter any errors, please fix them before submitting.

To submit your assignment for grading, save your work by clicking the 💾 icon at the top left, then click the <span style="color: blue; font-weight: bold;">Submit assignment</span> button at the top right. Good luck!

Everything below this is OPTIONAL and will not affect your grading in anyway.

Save your poem in the file!


```python
save_to_file(poem)
```

You can use the following button to download the file you just wrote above.

* Make sure to provide the right file name: `poem.txt` when asked!


```python
download_file()
```

## Mission Accomplished! 🎉

Congratulations on completing this stellar coding adventure! You've successfully used Python to explore a news article, extract key topics, and even generate a space-themed poem! As you continue your coding journey, remember that the possibilities are as boundless as the universe itself. 🚀 Keep exploring, keep creating, and never stop reaching for the stars! ✨
