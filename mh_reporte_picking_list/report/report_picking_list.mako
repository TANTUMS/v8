<html>
    <body>
        <table width="100%">
            <tr>
                <h1><p>Lista de Surtido</p></h1>

            </tr>
        </table>
        <table border="1.0" width="100%">
                <tr>
                    <th>name</th>
                    <th>code</th>
                    <th>date</th>
                </tr>
            %for picking in objects:
                <tr>
                    <td>${picking.name}</td>
                </tr>
                %endfor
            </table>
    </body>
</html>