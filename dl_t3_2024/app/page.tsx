

export default function Home({ routes }) {
  return (
    <div>
      <h1>My Homepage</h1>
      <h2>Available Routes:</h2>
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
