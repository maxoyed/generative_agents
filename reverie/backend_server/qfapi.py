from utils import qianfan_api_key, qianfan_secret_key
import qianfan

qianfan.AK(qianfan_api_key)
qianfan.SK(qianfan_secret_key)

chat_client = qianfan.ChatCompletion()
completions_client = qianfan.Completion()
model = {
    "chat": "Llama-2-70b-chat",
    "completion": "Llama-2-70b-chat"
}

def chat(prompt):
    resp = chat_client.do(model=model["chat"], messages=[{
        "role": "user",
        "content": prompt
    }])
    return resp.body["result"]

def completions(prompt, gpt_parameter = None):
    resp = completions_client.do(model=model["completion"], prompt=prompt)
    return resp.body["result"]

if __name__ == "__main__":
    print(f"### Completion Model:{model['completion']} ###\n\n")
    prompts = {
        "en": """
Name: Isabella Rodriguez
Age: 34
Innate traits: friendly, outgoing, hospitable
Learned traits: Isabella Rodriguez is a cafe owner of Hobbs Cafe who loves to make people feel welcome. She is always looking for ways to make the cafe a place where people can come to relax and enjoy themselves.
Currently: Isabella Rodriguez is planning on having a Valentine's Day party at Hobbs Cafe with her customers on February 14th, 2023 at 5pm. She is gathering party material, and is telling everyone to join the party at Hobbs Cafe on February 14th, 2023, from 5pm to 7pm.
Lifestyle: Isabella Rodriguez goes to bed around 11pm, awakes up around 6am.
Daily plan requirement: Isabella Rodriguez opens Hobbs Cafe at 8am everyday, and works at the counter until 8pm, at which point she closes the cafe.
Current Date: Monday February 13


In general, Isabella Rodriguez goes to bed around 11pm, awakes up around 6am.
Isabella's wake up hour:
""",
        "zh": """
姓名：伊莎贝拉·罗德里格斯
年龄：34
与生俱来的特质：友善、外向、好客
习得特质：伊莎贝拉·罗德里格斯是 Hobbs 咖啡馆的老板，喜欢让人们感到受欢迎。 她一直在寻找方法，让咖啡馆成为人们放松和享受的地方。
目前：伊莎贝拉·罗德里格斯计划于 2023 年 2 月 14 日下午 5 点在 Hobbs 咖啡馆与她的顾客举办情人节派对。 她正在收集派对材料，并告诉大家参加 2023 年 2 月 14 日下午 5 点至晚上 7 点在  Hobbs 咖啡馆举行的派对。
生活方式：伊莎贝拉·罗德里格斯晚上 11 点左右睡觉，早上 6 点左右起床。
每日计划要求：伊莎贝拉·罗德里格斯每天早上 8 点开放 Hobbs 咖啡馆，并在柜台工作到晚上 8 点，此时她会关闭咖啡馆。
当前日期： 2 月 13 日星期一


一般来说，伊莎贝拉·罗德里格斯晚上 11 点左右睡觉，早上 6 点左右起床。
伊莎贝拉的起床时间：
"""
    }
    print(f"#### EN_Q ####\n{prompts['en']} \n#### EN_A ####\n{completions(prompts['en'])}\n\n")
    print(f"#### ZH_Q ####\n{prompts['zh']} \n#### ZH_A ####\n{completions(prompts['zh'])}")