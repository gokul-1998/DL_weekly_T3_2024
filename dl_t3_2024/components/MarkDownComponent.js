// components/MarkdownComponent.js

import React from 'react';
import ReactMarkdown from 'react-markdown';
import fs from 'fs';
import path from 'path';

// Markdown Component using getStaticProps to fetch markdown content
const MarkdownComponent = ({ content }) => {
  return (
    <div>
      <ReactMarkdown>{content}</ReactMarkdown>
    </div>
  );
};

// Fetch Markdown file from the filesystem
export const getStaticProps = async () => {
  const filePath = path.join(process.cwd(), 'public', '001.md');
  const content = fs.readFileSync(filePath, 'utf8');
  
  return {
    props: {
      content, // Pass the content as props
    },
  };
};

export default MarkdownComponent;
