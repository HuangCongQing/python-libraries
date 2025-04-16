import time
import threading
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError

class VoiceSemanticListener:
    def __init__(self):
        self.recognizer = Recognizer()
        self.microphone = Microphone()
        self.is_listening = False
        self.callbacks = {
            "开始": [],
            "结束": []
        }
        self.any_text_callbacks = []  # 新增：所有文本的通用回调

        # 校准环境噪音
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def register_keyword_callback(self, keyword, callback):
        """注册关键词回调函数"""
        if keyword in self.callbacks:
            self.callbacks[keyword].append(callback)
        else:
            print(f"警告: 不支持的关键词 {keyword}")

    def register_any_text_callback(self, callback):
        """注册通用文本回调（监听所有识别内容）"""
        self.any_text_callbacks.append(callback)

    def _listen_loop(self):
        """后台监听循环"""
        with self.microphone as source:
            while self.is_listening:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=2)
                    text = self.recognizer.recognize_google(audio, language='zh-CN')
                    print(f"识别结果: {text}")

                    # 触发通用文本回调（无论是否含有关键词）
                    for callback in self.any_text_callbacks:
                        callback(text)  # 将完整文本传递给回调

                    # 语义匹配触发关键词回调
                    for keyword in self.callbacks:
                        if keyword in text:
                            for callback in self.callbacks[keyword]:
                                callback()

                except UnknownValueError:
                    pass  # 无有效语音输入
                except RequestError as e:
                    print(f"语音识别服务错误: {e}")
                except Exception as e:
                    print(f"未知错误: {e}")

    def start(self):
        """开始监听"""
        if not self.is_listening:
            self.is_listening = True
            self.thread = threading.Thread(target=self._listen_loop)
            self.thread.start()
            print("语音监听已启动")

    def stop(self):
        """停止监听"""
        if self.is_listening:
            self.is_listening = False
            self.thread.join()
            print("语音监听已停止")

# 使用示例 ==============================================
if __name__ == "__main__":
    # 定义共享变量（使用列表实现跨线程数据共享）
    speaker = [None]  # 用列表包装以实现引用传递

    def update_speaker(text):
        """通用回调函数：更新 speaker 变量"""
        speaker[0] = text
        print(f"[DEBUG] 当前 speaker 内容: {speaker[0]}")

    def on_start():
        print("检测到「开始」指令 → 执行启动操作")

    def on_end():
        print("检测到「结束」指令 → 执行终止操作")

    # 初始化监听器
    listener = VoiceSemanticListener()
    
    # 注册回调
    listener.register_keyword_callback("开始", on_start)
    listener.register_keyword_callback("结束", on_end)
    listener.register_any_text_callback(update_speaker)  # 注册通用文本监听

    # 开始监听
    listener.start()

    try:
        # 主循环监控 speaker 变化
        while True:
            current_speaker = speaker[0]
            if current_speaker:
                # 在此添加根据 speaker 内容执行的业务逻辑
                print(f"[主线程] 当前 speaker 最新值: {current_speaker}")
                
            time.sleep(0.5)  # 降低 CPU 占用
    except KeyboardInterrupt:
        listener.stop()