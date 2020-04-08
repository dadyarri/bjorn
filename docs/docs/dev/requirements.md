## Базовые зависимости

<table>
	<tr>
		<th>Пакет</th>
		<th>Версия</th>
	</tr>
	{% for requirement in requirements("requirements") %}
		<tr>
			<td>{{ requirement["package"] }}</td>
			<td>{{ requirement["version"] }}</td>
		</tr>
	{% endfor %}
</table>

## Зависимости для разработки

<table>
	<tr>
		<th>Пакет</th>
		<th>Версия</th>
	</tr>
	{% for requirement in requirements("dev_requirements") %}
		<tr>
			<td>{{ requirement["package"] }}</td>
			<td>{{ requirement["version"] }}</td>
		</tr>
	{% endfor %}
</table>