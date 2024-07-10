interface ChatMessageProps {
    text: string;
    isUser: boolean;
  }
  
  export default function ChatMessage({ text, isUser }: ChatMessageProps) {
    return (
      <div
        className={`flex ${
          isUser ? 'justify-end' : 'justify-start'
        } mb-2`}
      >
        <div
          className={`px-4 py-2 rounded-lg ${
            isUser ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-800'
          }`}
        >
          {text}
        </div>
      </div>
    );
  }
  