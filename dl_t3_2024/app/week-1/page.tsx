
export default async function Home() {
  const routes = await getRoutes(); // Fetch the folders in the component

  return (
    <div>
      <h1>My Homepage</h1>
      <h2>Available Folders:</h2>
      <ul>
        {routes.map(({ route }) => (
          <li key={route}>
            <a href={route}>{route}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}
