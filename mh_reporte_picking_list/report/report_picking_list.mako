<html>
    <body>
        <table  width="100%">
            <tr>
                <td  width="100%" colspan="5">
                    <h1><p>Lista de Surtido</p></h1>
                </td>
            </tr>
            <tr>
                <td width="100%" colspan="5">
                    <p>Este documento es de uso interno, no es un comprobante de envi&acuteo de producto, su uso es como lista de recoleccion para surtido de pedidos, no contiene instrucciones de envio.</p>
                </td>
            </tr>
            <tr>
               <td width="33.3%" align="center" colspan="1"> <p>Vendido a : ${objects.partner_id.name}</p></td>
               <td width="33.3%" align="center" colspan="1">Enviado a: ${objects.partner_id.mh_shipping_name}</td>
               <td width="33.3%" align="center" colspan="3">No Cliente :${objects.group_id.id_dim}</td>
            </tr>
            <tr>
                <td width="33.3%" align="center">Hoja de Recoleccion: ${objects.name}</td>
                <td width="33.3%" align="center"><font size="50">${objects.group_id.name}</font></td>
                <td width="33.3%" align="center" colspan="3"><p>Nova Orden:${objects.group_id.official_consecutive}</p></td>
            </tr>
            <tr>
                <td width="20%" colspan="1"><p>Tienda : ${objects.picking_type_id.warehouse_id.code}</p></td>
                <td width="20%" colspan="1"><p>Usuario : ${objects.create_uid.name}</p></td>
                <td width="20%" colspan="1"><p>Fecha : ${objects.date}</p></td>
                <td width="20%" colspan="1"><p>Prometido : ${objects.date_min}</p></td>
                <td width="20%" colspan="1" align="left"><font size="50"><p>DIM ${objects.group_id.id_dim}</p></font></td>
            </tr>
            <tr>
                    <td width="20%" align="center">Descripcion</td>
                    <td width="20%" align="center">No Art Cliente</td>
                    <td width="20%" align="center">Emb</td>
                    <td width="20%" align="center">UM</td>
                    <td width="20%" align="center"></td>
               
            </tr>
        %for line in objects.move_lines:
            <tr>
                <td width="20%" align="center">${line.product_id.name_template}</td>
                <td width="20%" align="center">${line.product_id.default_code}</td>
                <td width="20%" align="center">${line.product_qty}</td>
                <td width="20%" align="center">${line.product_id.product_tmpl_id.uom_id.name}</td>
                <td width="20%" align="center"><p>___________________________</p></td>
            </tr>
        %endfor
            <tr>
                <td width="20%" align="center"><p>Firma Chofer</p></td>
                <td width="20%" align="center"><p>Firma Cliente</p></td>
            </tr>
             <tr>
                <td width="20%" align="center"><p>___________________</p></td>
                <td width="20%" align="center"><p>___________________</p></td>
            </tr>
        </table>
    </body>
</html>