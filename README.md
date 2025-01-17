## Inspiration
It was in 2020, during the spread of the coronavirus pandemic, that everything changed. **Other illnesses, like cardiovascular diseases, were pushed** aside as hospitals struggled with an overwhelming lack of staff. This was one of the heartbreaking factors that led **to the loss of my grandfather**. Sadly, this is still happening today. Wouldn’t it be meaningful to help our communities and save lives by **creating a system that reasons like a group of doctor—ones** that can support those who need care the most?

## What it does
We’re not cardiologists, and we didn’t have the specialized knowledge to model cardiovascular diseases accurately. That’s why we decided to **combine machine learning with an automatic reasoner**. **We created an algorithm that translates the trees of a Random Forest model into s(CASP)-compatible rules**. We trained the Random Forest using a cardiac disease dataset, where each tree represents a doctor. We also developed a function to **model patients into s(CASP) format** and perform the query, allowing the system to reason and provide a diagnosis based on the criteria and experience of each doctor. 

Not content with that, we decided to apply **explainability** to our model through s(CASP), so instead of just a bunch of logical rules, it **explains in natural language** what each doctor said for each patient.
- **We can enter new patients**: Automatic translation to s(CASP).
- **Consult for our disease**: The reasoner will display the result in our web browser using natural language.
- **Consult for patients in our database**: Select a percentage of the database, automatically translate the patient, and infer using s(CASP).

## How we built it
We **trained a random forest** in Python on a cardiac dataset and then **translated each tree into s(CASP) rules using our custom algorithm**. We also created an algorithm to translate patients from the dataset into s(CASP) format and a function to request data when introducing a new patient. To improve explainability, we implemented a system to **translate s(CASP) rules into natural language**. We developed a **main program that integrates all** of the above functionalities. Finally, we set up a **consultation system in Python that communicates with s(CASP)** and provides the results in an HTML file, which is automatically opened in a **web browser**.

## Challenges we ran into
**Translating** from trees to s(CASP) and integrating Python with s(CASP) in the main program were some of the key challenges we faced. Working with medical data and mastering Prolog was no easy feat. Every bug felt like a mini boss battle, and the looming deadlines certainly kept us on our toes.

## Accomplishments that we're proud of
We’re proud of creating our own algorithms to translate models into s(CASP) and for successfully integrating them with our system.

## What we learned
**We learned that s(CASP) and explainability are game-changers**. Prolog helped us think critically and creatively, while our experience working together reinforced that teamwork truly makes a difference.

## What's next for Cardiolog
What’s next for Cardiolog? We’re refining the system and extending it to other diseases. Our goal is not only to assist healthcare professionals but to redefine how decisions are made in the field.

## Challenges we ran into
Translating from trees to s(CASP) and integrating Python with s(CASP) in the main program were some of the key challenges we faced. Working with medical data and mastering Prolog was no easy feat. Every bug felt like a mini boss battle, and the looming deadlines certainly kept us on our toes. **Also, we are a team from Spain and had to work late nights during exam periods**.

### Wanna tryout?
Be sure to change this: 
```python
   # Rute to scasp
  scasp_path = '/home/walter/.ciao/build/bin/scasp'  # put yours here
```
in `Main` -> `consulta_con_pacientes_introducido()`
