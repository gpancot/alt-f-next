#!/bin/sh

source ./common.sh
check_cookie
read_args

write_header "NZBget Setup"

NZBCONF=/etc/nzbget.conf
maindir=$(sed -n 's|^MainDir=\(.*\)|\1|p' $NZBCONF)

if ! rcnzbget status >& /dev/null; then
	webbut="disabled"
fi

cat<<-EOF
	<script type="text/javascript">
		function browse_dir_popup(input_id) {
			start_dir = document.getElementById(input_id).value;
			if (start_dir == "")
				start_dir="/mnt";
			window.open("browse_dir.cgi?id=" + input_id + "?browse=" + start_dir, "Browse", "scrollbars=yes, width=500, height=500");
			return false;
		}
	</script>

	<form name=nzbget action=nzbget_proc.cgi method="post" >
	<table>
	<tr><td>NZBget Folder</td>
	<td><input type=text size=32 id="conf_dir" name="conf_dir" value="$(httpd -e "$maindir")"></td>
	<td><input type=button onclick="browse_dir_popup('conf_dir')" value=Browse></td>
	</tr></table>
	
	<p><input type=submit name=submit value=Submit> $(back_button)
	<input type="submit" $webbut name=webPage value=WebPage>
	</form></body></html>
EOF