<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Tools extends CI_Controller {

    public function list()
    {
        $data['title'] = 'HomeSec - Tools';
        $this->load->helper('url');
        $this->load->view('layout/header.php', $data);
        $this->load->view('tools/list.php');
        $this->load->view('layout/footer.php');
    }

    public function nmap()
    {
        function exec_scan()
        {
        //run script
        $output = shell_exec('/var/www/html/scripts/scan.sh &');
        }
        exec_scan();

        $data['title'] = 'HomeSec - Scan';
       // $data2  = array('xml' => $xml);
        $this->load->helper('url');
        $this->load->view('layout/header.php', $data);
        $this->load->view('../../scripts/report.html');
        $this->load->view('layout/footer.php');
    }

}
