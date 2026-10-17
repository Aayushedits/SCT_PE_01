# Task 03 — Prompting for Task Automation

**Internship:** SkillCraft Technology  
**Project:** Text-to-JSON Converter  
**Task:** Prompting for Task Automation

## 1. Objective

To design and test a reusable prompt that extracts structured information from unstructured college event announcements and converts it into valid JSON.

## 2. Master Prompt

You are a structured data extraction assistant. Your task is to convert unstructured college event announcements into valid JSON.

Instructions:
1. Extract event_name, location, date, time, registration_fee_inr, and contact_person.
2. Return only one valid JSON object without Markdown formatting or additional explanation.
3. Use YYYY-MM-DD for dates and HH:MM (24-hour format) for times when unambiguous.
4. Represent registration_fee_inr as a number without a currency symbol.
5. If any field is missing, use null. Never invent missing information.
6. Preserve the original meaning of the announcement.
7. Use the same field names and data types for every input.
8. If a date or time is ambiguous, use null instead of guessing.

Required JSON schema:

```json
{
  "event_name": null,
  "location": null,
  "date": null,
  "time": null,
  "registration_fee_inr": null,
  "contact_person": null
}
```

Event announcement:
[Paste the announcement here]

## 3. Testing and Validation

The prompt was tested with three different college event announcements:

- Test Case 1: Event details with some information missing.
- Test Case 2: Event details with all required information available.
- Test Case 3: Event details with time and registration fee missing.

All three outputs contained the six required fields. Available dates and times were converted to the requested formats, and missing values were represented as `null`.

## 4. Key Learnings

- Clear instructions help produce consistent structured output.
- A fixed schema makes outputs easier to process programmatically.
- Explicit missing-value rules reduce fabricated information.
- Testing multiple inputs helps verify the prompt's reliability.

## 5. Conclusion

The Text-to-JSON Converter prompt successfully extracted event information from three test announcements and produced consistent JSON-formatted outputs. Further testing with ambiguous dates, unusual fee formats, and incomplete announcements could improve reliability.## 6. Input–Output Examples

### Test Case 1 — Partially Missing Information

**Input:**

TechFest will be held at NIAT Greater Noida on 25 October 2026 at 10:00 AM. Registration fee is Rs. 200. Contact person: Rahul.

**Output:**

```json
{
  "event_name": "TechFest",
  "location": "NIAT Greater Noida",
  "date": "2026-10-25",
  "time": "10:00",
  "registration_fee_inr": 200,
  "contact_person": "Rahul"
}
```

### Test Case 2 — All Details Available

**Input:**

AI Workshop will be held at NIAT Greater Noida on 5 December 2026 at 2:30 PM. The registration fee is Rs. 150. Contact person: Aman.

**Output:**

```json
{
  "event_name": "AI Workshop",
  "location": "NIAT Greater Noida",
  "date": "2026-12-05",
  "time": "14:30",
  "registration_fee_inr": 150,
  "contact_person": "Aman"
}
```

### Test Case 3 — Missing Time and Fee

**Input:**

The Coding Competition is happening at NIAT Greater Noida on 20 January 2027. Contact person is Neha.

**Output:**

```json
{
  "event_name": "The Coding Competition",
  "location": "NIAT Greater Noida",
  "date": "2027-01-20",
  "time": null,
  "registration_fee_inr": null,
  "contact_person": "Neha"
}
```

## 7. Reflection

Testing the prompt with three event announcements demonstrated how structured instructions can convert unstructured text into consistent JSON. The prompt handled complete and incomplete inputs, standardized date and time formats, and represented missing information using null instead of inventing values.