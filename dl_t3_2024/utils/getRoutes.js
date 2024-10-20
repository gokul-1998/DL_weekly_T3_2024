import fs from 'fs';
import path from 'path';

export const getRoutes = async () => {
  const appDir = path.join(process.cwd(), 'app');
  const items = fs.readdirSync(appDir, { withFileTypes: true });

  // Filter only directories
  const routes = items
    .filter(item => item.isDirectory())
    .map(folder => ({
      route: `/${folder.name}`
    }));

  return routes;
};
