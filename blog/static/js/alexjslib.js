/**
 * Created by alex on 16/4/4.
 */

function logincheck($)
    {
        $.validator.addMethod('login_username', function (value) {
        return /^\s*[a-zA-Z]{1}([a-zA-Z0-9]|[_]){2,19}\s*$/.test(value);
        }, '输入3-20个，以字母开头，可以字母、数字、空格,_');

        $.validator.addMethod('login_password', function (value) {
        return /^[a-zA-Z]{1}([\@A-Za-z0-9\!\#\$\%\^\&\*\.\~]){4,19}$/.test(value);
        }, '输入5-20个，以字母开头');

        // Reveal Login form
        setTimeout(function(){ $(".fade-in-effect").addClass('in'); }, 1);
        // Validation and Ajax action
        $("form#login").validate({
            rules: {
                username: {
                    required: true,
                    login_username:'输入3-20个，以字母开头，可以字母、数字、_'
                },

                passwd: {
                    required: true,
                    login_password:'输入5-20个，以字母开头'
                }
            },

            messages: {
                username: {
                    required: '请输入用户名'
                },

                passwd: {
                    required: '密码不能空'
                }

            },

            submitHandler: function(form)
            {
                var opts = {
                    "closeButton": true,
                    "debug": false,
                    "positionClass": "toast-top-full-width",
                    "onclick": null,
                    "showDuration": "300",
                    "hideDuration": "1000",
                    "timeOut": "5000",
                    "extendedTimeOut": "1000",
                    "showEasing": "swing",
                    "hideEasing": "linear",
                    "showMethod": "fadeIn",
                    "hideMethod": "fadeOut"
                };

                $.ajax({
                    url: "/blog/login",
                    method: 'POST',
                    dataType: 'json',
                    data: {
                        do_login: true,
                        username: $(form).find('#username').val().replace(/(^\s*)|(\s*$)/g, ""),
                        passwd: $(form).find('#passwd').val().replace(/(^\s*)|(\s*$)/g, "")
                    },
                    success: function(result){
                        if (result.res==1){
                             //alert('登陆成功!');
                           show_loading_bar({
                            delay: .5,
                            pct: 100,
                            finish: function() {
                                window.location.href = "/blog/index.html"
                            }
                           });
                         }else if(result.res==0){
                             //alert("密码不正确");
                             //toastr.error("密码不正确", "Error", opts);
                             //$passwd.select();
                             $(".errors-container").html('<div class="alert alert-danger">\
                                <button type="button" class="close" data-dismiss="alert">\
                                    <span aria-hidden="true">&times;</span>\
                                    <span class="sr-only">Close</span>\
                                </button>\
                                ' + "密码不正确" + '\
                            </div>');
                           $(".errors-container .alert").hide().slideDown();
                            $(form).find('#passwd').select();

                         }else if(result.res==2){
                             //alert("用户名不存在");
                            // toastr.error("用户名不存在", "Error", opts);

                           $(".errors-container").html('<div class="alert alert-danger">\
                                <button type="button" class="close" data-dismiss="alert">\
                                    <span aria-hidden="true">&times;</span>\
                                    <span class="sr-only">Close</span>\
                                </button>\
                                ' + "用户名不存在" + '\
                            </div>');
                           $(".errors-container .alert").hide().slideDown();
                            $(form).find('#passwd').select();
                         }else if(result.res==3){
                            $(".errors-container").html('<div class="alert alert-danger">\
                                <button type="button" class="close" data-dismiss="alert">\
                                    <span aria-hidden="true">&times;</span>\
                                    <span class="sr-only">Close</span>\
                                </button>\
                                ' + "审核失败，请重新注册商铺" + '\
                            </div>');
                           $(".errors-container .alert").hide().slideDown();
                        }else if(result.res==4){
                             $(".errors-container").html('<div class="alert alert-danger">\
                                <button type="button" class="close" data-dismiss="alert">\
                                    <span aria-hidden="true">&times;</span>\
                                    <span class="sr-only">Close</span>\
                                </button>\
                                ' + "等待审核中..." + '\
                            </div>');
                           $(".errors-container .alert").hide().slideDown();
                        }else if(result.res==4){
                             $(".errors-container").html('<div class="alert alert-danger">\
                                <button type="button" class="close" data-dismiss="alert">\
                                    <span aria-hidden="true">&times;</span>\
                                    <span class="sr-only">Close</span>\
                                </button>\
                                ' + "系统错误" + '\
                            </div>');
                           $(".errors-container .alert").hide().slideDown();
                        }


                   }

                });

            }
        });

        // Set Form focus
    //	$("form#login .form-group:has(.form-control):first .form-control").focus();
    }

