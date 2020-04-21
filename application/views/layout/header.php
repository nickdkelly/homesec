<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title><?php if ($title) { echo $title; } else { echo 'HomeSec'; } ?></title>

        <meta name="referrer" content="no-referrer"/>

        <link rel="icon" href="../resources/favicon.ico" type="image/x-icon" />

        <link rel="stylesheet" type="text/css" href="../global.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans&display=swap">
        <link rel="stylesheet" type="text/css" href="../semantic/semantic.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"/>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous"/>
        <link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap.min.css" type="text/css" integrity="sha384-VEpVDzPR2x8NbTDZ8NFW4AWbtT2g/ollEzX/daZdW/YvUBlbgVtsxMftnJ84k0Cn" crossorigin="anonymous"/>

        <script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha384-fJU6sGmyn07b+uD1nMk7/iSb4yvaowcueiQhfVgQuD98rfva8mcr1eSvjchfpMrH" crossorigin="anonymous"></script>
        <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js" integrity="sha384-rgWRqC0OFPisxlUvl332tiM/qmaNxnlY46eksSZD84t+s2vZlqGeHrncwIRX7CGp" crossorigin="anonymous"></script>
        <script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap.min.js" integrity="sha384-7PXRkl4YJnEpP8uU4ev9652TTZSxrqC8uOpcV1ftVEC7LVyLZqqDUAaq+Y+lGgr9" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

        <script src="../semantic/semantic.min.js"></script>
    </head>

    <body>

    <div class="ui grid">
        <div class="ui centered ten wide column" style="margin-bottom:150px;">
            <div class="ui fixed teal inverted menu">
                <div class="ui container">
                    <div class="ui header item" style="margin-left:-415px; margin-right: 190px;">
                        <img class="logo" src="../resources/main_logo_transparency.png">
                        HomeSec - Accessible Security
                    </div>
                    <a href="<?php echo base_url();?>" class="ui <?php if(!$this->uri->segment(1)) { echo 'teal active ' ;} ?> item">Home</a>
                    <a href="<?php echo base_url() . 'Pages/learn';?>" class="ui <?php if($this->uri->segment(2) == 'learn') { echo 'teal active ' ;} ?> item">Learn</a>
                    <a href="<?php echo base_url() . 'Tools/list'; ?>" class="ui <?php if($this->uri->segment(1) == 'Tools') { echo 'teal active ' ;} ?> item">Tools</a>
                    <a href="<?php echo base_url() . 'Pages/faq';?>" class="ui <?php if($this->uri->segment(2) == 'faq') { echo 'teal active ' ;} ?> item" >FAQ</a>

                </div>
            </div>
           <!-- old button style menu  <div class="ui teal large four item menu" style="margin-bottom:30px;margin-top:100px;overflow: auto;">
                <a href="<?php echo base_url();?>" class="ui <?php if(!$this->uri->segment(1)) { echo 'teal active ' ;} ?> item">Home</a>
                <a href="<?php echo base_url() . 'Pages/learn';?>" class="ui <?php if($this->uri->segment(2) == 'learn') { echo 'teal active ' ;} ?> item">Learn</a>
                <a href="<?php echo base_url() . 'Tools/list'; ?>" class="ui <?php if($this->uri->segment(1) == 'Tools') { echo 'teal active ' ;} ?> item">Tools</a>
                <a href="<?php echo base_url() . 'Pages/faq';?>" class="ui <?php if($this->uri->segment(2) == 'faq') { echo 'teal active ' ;} ?> item" >FAQ</a>
            </div> -->
        </div>


