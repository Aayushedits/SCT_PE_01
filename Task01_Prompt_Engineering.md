# Task 01 – Writing Better Prompts

## Prompt 1: Artificial Intelligence

### 1. Vague Prompt

**Prompt:**

> Explain artificial intelligence.

### Output:

Artificial Intelligence (AI) is a branch of computer science that focuses on creating machines and software that can perform tasks that normally require human intelligence. These tasks include learning from data, understanding language, recognizing images, solving problems, making decisions, and predicting outcomes.

AI is used in many areas such as:

- Voice assistants like Siri and Alexa
- Recommendation systems on YouTube and Netflix
- Self-driving technologies
- Chatbots
- Medical diagnosis systems
- Fraud detection in banking

In simple words, AI enables computers to learn, reason, and perform tasks in ways that resemble human intelligence.

---

### 2. Improved Prompt

**Prompt:**

> Explain artificial intelligence in 5 simple bullet points for a beginner. Include one real-world example and use easy English.

### Output:

- AI is a technology that allows computers to perform tasks that usually require human intelligence.
- AI can learn from data and use that information to make decisions or predictions.
- AI can understand language, recognize images, and solve different types of problems.
- AI is used in everyday life in apps, websites, smartphones, and many other systems.
- The main goal of AI is to help computers perform tasks intelligently and efficiently.

**Real-world example:**

A recommendation system on YouTube uses AI to suggest videos based on what you have watched or searched for before.

---

## Prompt 2: Pollution

### 1. Vague Prompt

**Prompt:**

> Write something about pollution.

### Output:

Pollution is the introduction of harmful substances into the environment. It can affect air, water, and land, causing problems for humans, animals, and plants.

Air pollution is caused by vehicles, factories, and burning fuels. Water pollution can result from industrial waste, sewage, and plastic. Land pollution is often caused by improper waste disposal and excessive use of chemicals.

Pollution can lead to health problems, environmental damage, and climate-related issues. Reducing pollution requires proper waste management, cleaner energy sources, recycling, and public awareness.

---

### 2. Improved Prompt

**Prompt:**

> Write a 120-word explanation of air pollution for a college student. Include 3 major causes, 2 effects, and 2 practical solutions in simple English.

### Output:

Air pollution occurs when harmful gases, particles, and chemicals enter the air and make it unsafe for living beings.

**3 Major Causes:**

1. Vehicle emissions from cars, buses, and trucks.
2. Smoke and harmful gases released by factories and industries.
3. Burning coal, wood, garbage, and other fuels.

**2 Effects:**

1. It can cause breathing problems and other health issues.
2. It can damage plants, animals, and the environment.

**2 Practical Solutions:**

1. Use public transport, bicycles, and cleaner vehicles.
2. Use renewable energy and reduce unnecessary fuel burning.

Reducing air pollution requires cooperation between individuals, industries, and governments. Awareness and responsible actions can help create cleaner and healthier communities for everyone.

---

## Prompt 3: Python Program

### 1. Vague Prompt

**Prompt:**

> Make a Python program.

### Output:

A Python program is a set of instructions written in the Python programming language to perform a specific task.

For example:

```python
print("Hello, World!")
```

This program displays "Hello, World!" on the screen. Python can be used to create many types of programs, including calculators, games, websites, automation tools, and data analysis applications.

---

### 2. Improved Prompt

**Prompt:**

> Write a beginner-friendly Python program that takes 5 numbers as input, calculates their average, and displays the result. Explain the code in 3 short points.

### Output:

```python
numbers = []

for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

average = sum(numbers) / 5

print("Average:", average)
```

**Explanation:**

1. The program takes 5 numbers from the user and stores them in a list.
2. `sum(numbers) / 5` calculates the average of the five numbers.
3. The calculated average is displayed on the screen.

---

# Comparison of Vague and Improved Prompts

| Prompt | Vague Prompt | Improved Prompt | Main Difference |
|---|---|---|---|
| 1. Artificial Intelligence | General explanation of AI | Specifies beginner level, 5 points, easy English, and an example | More clear and structured |
| 2. Pollution | General information about pollution | Specifies air pollution, causes, effects, solutions, and a word limit | More specific and focused |
| 3. Python Program | Does not specify what program to create | Specifies input, calculation, output, and explanation | Gives clear instructions |

## How Prompt Design Affects LLM Behavior

Vague prompts give the AI more freedom to decide what information and format to provide. As a result, the response may be general or different from what the user expects.

Improved prompts provide clear instructions about the topic, audience, format, length, and required information. This helps the AI generate more relevant, focused, and useful responses.

## Key Observations

- Clear prompts produce more relevant answers.
- Specific instructions improve the structure of the response.
- Mentioning the target audience helps control the difficulty level.
- Giving output requirements makes the response more predictable.
- Vague prompts can produce broad and less focused answers.

## Conclusion

Prompt design has a direct effect on the quality and usefulness of an LLM response. A well-designed prompt provides context and clear requirements, helping the AI generate a more accurate, focused, and suitable answer.

This task demonstrates that adding specific instructions such as audience, format, length, required information, and output expectations can significantly improve the quality of an LLM response.