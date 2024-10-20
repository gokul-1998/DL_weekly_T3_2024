import fs from 'fs';
import path from 'path';

export const getStaticProps = async () => {
  const pagesDir = path.join(process.cwd(), 'pages');
  const filenames = fs.readdirSync(pagesDir);

  // Filter out the API folder and Next.js special files (like _app.js, _document.js)
  const routes = filenames
    .filter(file => !file.startsWith('_') && file.endsWith('.js'))
    .map(file => ({
      route: file === 'index.js' ? '/' : `/${file.replace('.js', '')}`
    }));

  return {
    props: {
      routes
    }
  };
};
