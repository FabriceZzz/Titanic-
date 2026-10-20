import pandas as pd
import logging

logging.basicConfig(
    filename='clean.log',            # 账本记在哪？记在当前目录的 clean.log 文件里
    level=logging.INFO,              # 记账级别：INFO（记普通信息）及以上
    format='%(asctime)s - %(levelname)s - %(message)s'  # 记账格式：时间 - 级别 - 具体内容
)

def main():
    logging.info('=== 开始执行数据清洗任务 ===')

    try:
        df = pd.read_csv('train.csv')
        # 用中位数填充Age
        df['Age'] = df['Age'].fillna(df['Age'].median())
        # 用众数填充Embarked
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
        # 删除缺失严重的Cabin列
        df = df.drop('Cabin', axis=1)

        # 把清洗好的数据存下来
        df.to_csv('train_cleaned.csv', index=False)

        # 4. 用 logging 记录成功状态
        logging.info(f"清洗成功！数据形状: {df.shape}")

    except Exception as e:
        # 如果报错了，把错误原因写进日志
        logging.error(f"清洗失败！错误信息: {e}")

if __name__ == "__main__":
    main()