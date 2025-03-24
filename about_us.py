import streamlit as st

def about_us_layout(vn):
    text = """

    # About Us

    ## io.net: Revolutionizing Access to GPU Computing

    At io.net, we're on a mission to democratize access to GPU computing power. Our decentralized network aggregates underutilized GPUs from independent data centers, crypto miners, and individual owners, transforming them into a robust, scalable infrastructure. This approach not only addresses the global GPU shortage but also empowers AI startups and developers with affordable, scalable compute resources. :contentReference[oaicite:0]{index=0}

    ## Our Origins

    Before June 2022, io.net focused on developing institutional-grade quantitative trading systems for both the U.S. stock market and the cryptocurrency market. Our primary challenge was constructing the infrastructure necessary to accommodate our complex needs, which included a robust backend trading system with significant computational power. 

    ## IO Intelligence: Empowering Developers with AI Tools

    Building on our decentralized GPU network, we've launched IO Intelligence—an AI infrastructure and API platform that democratizes access to advanced AI models and agents. IO Intelligence enables users to seamlessly integrate pre-trained open-source models and custom AI agents into their applications via straightforward API calls. 

    ### Explore AI Models and Agents

    With IO Intelligence, you can:

    - **Access Pre-Trained Models**: Utilize a diverse range of open-source AI models tailored to various applications.
    - **Deploy Custom AI Agents**: Integrate intelligent agents capable of performing specific tasks, enhancing automation and efficiency.

    ### Get Started with Free Credits

    We're excited to offer new users free credits to experience the capabilities of IO Intelligence firsthand. Sign up today to explore our AI models and agents, and discover how they can transform your workflows.

    *Note: For detailed information on creating an API key and integrating IO Intelligence into your projects, please refer to our [documentation](https://docs.io.net/docs/io-intelligence).*


    https://io.net/about-us


    """
    return st.markdown(text)