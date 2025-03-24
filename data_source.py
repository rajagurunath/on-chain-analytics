import streamlit as st


def data_source_layout(vn):
    text = """
    ## Blockchain Datasource
    - In order to perform analytics over block chain data at real time, we need to connect to some datasources
    - we can use free datasource provided by clickhouse and goldsky combination called cryptohouse.

    ## CryptoHouse: Free Blockchain Analytics Powered by ClickHouse and Goldsky

    [CryptoHouse](https://crypto.clickhouse.com) is a free blockchain analytics platform developed collaboratively by 
    ClickHouse and Goldsky. It offers real-time access to blockchain data, enabling users to execute SQL queries directly on datasets from networks like Solana and Ethereum. This service democratizes blockchain analytics by providing instant query responses without the need for scheduled, asynchronous queries. :contentReference[oaicite:0]{index=0}

    ### Available Datasets

    As of now, CryptoHouse provides access to several datasets, including:

    - **Solana**: Blocks, transactions, token transfers, block rewards, accounts, and tokens.
    - **Ethereum**: Similar datasets are available, with plans to expand to additional blockchains in the future.

    These datasets are continuously updated in real-time, ensuring users have access to the most current information. :contentReference[oaicite:1]{index=1}

    ## Especially about solana since IONET is built on solana, following data is available for solana,

    |    | Dataset                             | Description                                                                                                                                                      |
    |---:|:------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |  0 | Edge Accounts                       | Contains details of all active accounts on the Solana blockchain, including balance and owner information. Live data from slot 271611201.                        |
    |  1 | Edge Blocks                         | Metadata for each block on the chain including hashes, transaction count, difficulty, and gas used. Live data from slot 271611201.                               |
    |  2 | Edge Instructions                   | Specific operations within transactions that describe the actions to be performed on the Solana blockchain. Live data from slot 271611201.                       |
    |  3 | Edge Rewards                        | Records of rewards distributed to validators for securing and validating the Solana network. Live data from slot 271611201.                                      |
    |  4 | Edge Token Transfers                | Transactions involving the movement of tokens between accounts on the Solana blockchain. Live data from slot 271611201.                                          |
    |  5 | Edge Tokens                         | Information about different token types issued on the Solana blockchain, including metadata and supply details. Live data from slot 271611201.                   |
    |  6 | Edge Transactions                   | Enriched transaction data including input, value, from and to address, and metadata for the block, gas and receipt. Live data from slot 271611201.               |
    |  7 | Edge Transactions with Instructions | Enriched transaction data including instructions, input, value, from and to address, and metadata for the block, gas and receipt. Live data from slot 316536533. |    

    For writing custom queries on top of solana data , please visit [CryptoHouse](https://crypto.clickhouse.com),
    if you found some interesting questions and relevant answers please add those question,sql pair in our training page. 
    """
    return st.markdown(text)
