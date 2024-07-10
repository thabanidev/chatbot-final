"use client"
import ChatInput from '@/components/ChatInput';
import ChatMessage from '@/components/ChatMessage';
import { useState, useEffect, useRef } from 'react';
import { UserButton } from '@clerk/nextjs';

export default function Home() {
  const [messages, setMessages] = useState<
    { text: string; isUser: boolean }[]
  >([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Scroll to the bottom of the chat window when new messages are added
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async (message: string) => {
    setIsLoading(true); // Start loading
    setMessages([...messages, { text: message, isUser: true }]);

    try {
      const response = await fetch(`http://127.0.0.1:5000/api/chat?msg=${message}`);
      const data = await response.json();
      setMessages([
        ...messages,
        { text: message, isUser: true },
        { text: data.response, isUser: false },
      ]);
    } catch (error) {
      console.error('Error fetching chatbot response:', error);
      setMessages([
        ...messages,
        { text: message, isUser: true },
        { text: 'Sorry, I am having trouble processing your request.', isUser: false },
      ]);
    } finally {
      setIsLoading(false); // Stop loading
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center ">
      <div className="container mx-auto p-4 w-full max-w-xl">
        <div className="flex justify-between items-center">
          <h1 className="text-3xl font-bold mb-4">AI Chatbot</h1>
          <UserButton />
        </div>
        <div className="bg-white rounded-lg shadow-md p-4 w-full">
          <div className="h-96 overflow-y-auto mb-4">
            {messages.map((msg, index) => (
              <ChatMessage key={index} text={msg.text} isUser={msg.isUser} />
            ))}
            <div ref={messagesEndRef} /> {/* For scrolling to the bottom */}
          </div>
          <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
        </div>
      </div>
    </main>
  );
}
