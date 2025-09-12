##ai智能体web端
# app.py
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.chat_models import ChatZhipuAI
import streamlit as st  # 导入Streamlit

# 设置页面标题和图标
st.set_page_config(page_title="AI智能助手", page_icon="💩")

# 加载环境变量
load_dotenv()  # 指定env路径
api_key = os.getenv("ZHIPUAI_API_KEY")

if not api_key:
    st.error("未找到 ZHIPUAI_API_KEY。请在本地创建 .env 文件或在云端设置 Secrets。")
    st.stop() # 停止应用

# 初始化模型和代理（使用缓存避免重复初始化）
@st.cache_resource
def load_ai_agent():
    """加载AI代理并缓存,提升性能"""
    try:
        llm = ChatZhipuAI(
            model='glm-4',
            zhipuai_api_key=api_key,
        )
        
        tools = load_tools(["llm-math", "ddg-search"], llm=llm)
        
        agent = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,  # 网页端不需要显示详细思考过程
            handle_parsing_errors=True  # 添加错误处理
        )
        return agent
    except Exception as e:
        st.error(f"初始化AI代理失败: {e}")
        return None

# 初始化会话状态，用于存储聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 网页标题和描述
st.title("💩 AI煞笔助手")
st.markdown("我可以帮您解答问题、进行数学计算和网络搜索。")

# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入框
if prompt := st.chat_input("请输入您的问题..."):
    # 添加用户消息到历史
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 获取AI回复
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):  # 显示加载动画
            try:
                # 加载代理
                agent = load_ai_agent()
                
                if agent:
                    # 运行代理获取回复
                    response = agent.run(prompt)
                    
                    # 显示回复
                    st.markdown(response)
                    
                    # 添加AI回复到历史
                    st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    st.error("AI代理未正确初始化,请检查API密钥。")
                    
            except Exception as e:
                error_msg = f"抱歉，处理您的请求时出错了: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# 侧边栏信息
with st.sidebar:
    st.header("ℹ️ 关于")
    st.markdown("""
    **功能特点：**
    - 💬 多轮对话
    - 🔢 数学计算
    - 🌐 网络搜索
    - 🧠 智能问答
    """)
    
    # 清空聊天历史按钮
    if st.button("清空聊天记录"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")

    st.caption("Powered by ZhipuAI GLM-4 & LangChain to luoyong")
