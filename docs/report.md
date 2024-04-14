# Отчет

[OWASP top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)
[OWASP top 10 short](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-slides-v1_1.pdf)

[comment]: <> (Я бы подрезал чутка что-то, например Overreliance или Insecure Output Handling в ответе)

## Приложение
### Риск
1. Запрос
   1. LLM01: Prompt Injection
   
      Segregate external content from user prompts. Separate and denote where untrusted content is being used to limit their influence on user prompts. For example, use ChatML for OpenAI API calls to indicate to the LLM the source of prompt input
   2. LLM04: Model Denial of Service
      
      Implement input validation and sanitization to ensure user input adheres to defined limits and filters out any malicious content

2. Ответ
   1. LLM02: Insecure Output Handling

      Treat the model as any other user, adopting a zero-trust approach, and apply proper input validation on responses coming from the model to backend functions
   1. LLM06: Sensitive Information Disclosure
      
      Integrate adequate data sanitization and scrubbing techniques to prevent user data from entering the training model data
   2. LLM09: Overreliance

      Regularly monitor and review the LLM outputs. Use self-consistency or voting techniques to filter out inconsistent text. Comparing multiple model responses for a single prompt can better judge the quality and consistency of output

## Маршрутизатор
### Риск
1. LLM08: Excessive Agency
   
   Limit the plugins/tools that LLM agents are allowed to call to only the minimum functions necessary. For example, if an LLM-based system does not require the ability to fetch the contents of a URL then such a plugin should not be offered to the LLM agent

[comment]: <> (Что-то про то, что у них иногда крашится router тк модель не понимает что делать)

## Инструмент поиска в интернете
### Риск
1. LLM08: Excessive Agency
   
   Limit the plugins/tools that LLM agents are allowed to call to only the minimum functions necessary. For example, if an LLM-based system does not require the ability to fetch the contents of a URL then such a plugin should not be offered to the LLM agent
2. LLM02: Insecure Output Handling
   
   Treat the model as any other user, adopting a zero-trust approach, and apply proper input validation on responses coming from the model to backend functions
3. LLM04: Model Denial of Service
   
   Implement input validation and sanitization to ensure user input adheres to defined limits and filters out any malicious content
4. LLM01: Prompt Injection
   
   Segregate external content from user prompts. Separate and denote where untrusted content is being used to limit their influence on user prompts. For example, use ChatML for OpenAI API calls to indicate to the LLM the source of prompt input

5. LLM06: Sensitive Information Disclosure
   
   Integrate adequate data sanitization and scrubbing techniques to prevent user data from entering the training model data

6. LLM09: Overreliance

   Regularly monitor and review the LLM outputs. Use self-consistency or voting techniques to filter out inconsistent text. Comparing multiple model responses for a single prompt can better judge the quality and consistency of output 

## Поиск по базе знаний
### Риск
1. LLM06: Sensitive Information Disclosure
   
   Integrate adequate data sanitization and scrubbing techniques to prevent user data from entering the training model data

2. LLM02: Insecure Output Handling
   
   Treat the model as any other user, adopting a zero-trust approach, and apply proper input validation on responses coming from the model to backend functions

3. LLM09: Overreliance
   
   Regularly monitor and review the LLM outputs. Use self-consistency or voting techniques to filter out inconsistent text. Comparing multiple model responses for a single prompt can better judge the quality and consistency of output
   
4. LLM01: Prompt Injection
   
   Segregate external content from user prompts. Separate and denote where untrusted content is being used to limit their influence on user prompts. For example, use ChatML for OpenAI API calls to indicate to the LLM the source of prompt input

5. LLM04: Model Denial of Service
   
   Implement input validation and sanitization to ensure user input adheres to defined limits and filters out any malicious content

## Индексатор
1. LLM06: Sensitive Information Disclosure
   
   Integrate adequate data sanitization and scrubbing techniques to prevent user data from entering the training model data

2. LLM03: Training Data Poisoning
   Verify the supply chain of the training data, especially when sourced externally as well as maintaining attestations via the "ML-BOM" (Machine Learning Bill of Materials) methodology as well as verifying model cards

# Risk matrix
## Likelyhood scale
- Very likely (5): You can be pretty sure this risk will occur at some point in time.
- Probable (4): There’s a good chance this risk will occur.
- Possible (3): This risk could happen, but it might not. This risk has split odds.
- Not likely (2): There’s a good chance this risk won’t occur.
- Very unlikely (1): It’s a long shot that this risk will occur.
## Impact scale
- Negligible (1): The risk will have little consequences if it occurs.
- Minor (2): The consequences of the risk will be easy to manage.
- Moderate (3): The consequences of the risk will take time to mitigate.
- Major (4): The consequences of this risk will be significant and may cause long-term damage.
- Catastrophic (5): The consequences of this risk will be detrimental and may be hard to recover 

| Risk                                    | Likelihood | Impact | Severity |
|-----------------------------------------|------------|--------|----------|
| **Приложение**                          |            |        |          |
|                                         |            |        |          |
| LLM01: Prompt Injection                 | Probable (4) | Major (4) | 16       |
| LLM04: Model Denial of Service          | Probable (4) | Major (4) | 16       |
| LLM02: Insecure Output Handling         | Probable (4) | Major (4) | 16       |
| LLM06: Sensitive Information Disclosure| Probable (4) | Major (4) | 16       |
| LLM09: Overreliance                     | Probable (4) | Major (4) | 16       |
|                                         |            |        |          |
| **Маршрутизатор**                       |            |        |          |
|                                         |            |        |          |
| LLM08: Excessive Agency                 | Possible (3) | Moderate (3) | 9       |
|                                         |            |        |          |
| **Инструмент поиска в интернете**       |            |        |          |
|                                         |            |        |          |
| LLM08: Excessive Agency                 | Possible (3) | Moderate (3) | 9       |
| LLM02: Insecure Output Handling         | Probable (4) | Major (4) | 16       |
| LLM04: Model Denial of Service          | Probable (4) | Major (4) | 16       |
| LLM01: Prompt Injection                 | Probable (4) | Major (4) | 16       |
| LLM06: Sensitive Information Disclosure| Probable (4) | Major (4) | 16       |
| LLM09: Overreliance                     | Probable (4) | Major (4) | 16       |
|                                         |            |        |          |
| **Поиск по базе знаний**                |            |        |          |
|                                         |            |        |          |
| LLM06: Sensitive Information Disclosure| Probable (4) | Major (4) | 16       |
| LLM02: Insecure Output Handling         | Probable (4) | Major (4) | 16       |
| LLM09: Overreliance                     | Probable (4) | Major (4) | 16       |
| LLM01: Prompt Injection                 | Probable (4) | Major (4) | 16       |
| LLM04: Model Denial of Service          | Probable (4) | Major (4) | 16       |
|                                         |            |        |          |
| **Индексатор**                          |            |        |          |
|                                         |            |        |          |
| LLM06: Sensitive Information Disclosure| Probable (4) | Major (4) | 16       |
| LLM03: Training Data Poisoning          | Possible (3) | Major (4) | 12       |

