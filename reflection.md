# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  Response: It told me to guess a number from 1-100 and it gave me 7 attempts.Difficulty was set to normal by default but i was able to change the difficulty if I wanted to via the drop down menu on the leftside. On that same leftside I could see my attempts left but there it said 8 and not 7. The show hint button worked fine and so did the submit answer button, not too sure on the new game button that one was a bit tricky to figure out if it was working or not. My attempts off by like one or two numbers. 
  
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
 
  Response: whenever I typed in my first guess it told me to go higher and when i did it told me to go higher again. Then I typed in a lower number and it started telling me to go lower. So I believe the hints were a bit off maybe telling me to go high when i typed in a bigger number and lower when I typed in a smaller number. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  Response: The AI tool I used for this project is Claude. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Response : The AI suggested that the number of tries was incorrect because the session attempts was set to 1 instead of 0. I checked to verify and agreed that the suggestion was correct! Claude demonstrated me the line of code that was causing this bug and explained to me why it should be set to 0 and showed me an example. I then went to check on the game and verified it was correct. I got even further verification once it was fixed and the attempts adjusted correctly. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Response: AI actually did not give me a incorrect or misleading suggestion! 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  Response: I decided a bug was really fixed after making sure my code was correct and tested several times.
- Describe at least one test you ran (manual or using pytest)   
  and what it showed you about your code.
  Response: I actually used pytest to see if the hints were fixed or not and was successful with fixing them! it showed me that the previous code was keeping me from getting near the correct answer. 
- Did AI help you design or understand any tests? How?
  Response: It was my first time using pytest so it was very helpful and cool to see. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  Response: The secret number changed in the original app because streamlit keeps re-running the scrip.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Response: think of it like a recipe card when something changes you start from the beggining to see the final recipe. 
- What change did you make that finally gave the game a stable secret number?
  Response: Fixing the hints helped a lot as well as the number of attemtps used.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Response: Getting more familiar with git for sure is something i want to get better at and reuse later on.
- What is one thing you would do differently next time you work with AI on a coding task?
  Response: Honestly? Using it sooner. This was much more efficent.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  Response: I dont think using AI makes you a poser anymore if anything you're just adapting with the times. You still have to understand what is generated for your project to work.
