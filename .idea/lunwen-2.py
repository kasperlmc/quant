#coding=gbk
import csv
s='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <META http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>�ĸ￪�������й�������ᱣ���ƶȵķ�չ��Ｐ����˼�� - �й�֪��
        </title>
    <link rel="stylesheet" type="text/css" href="http://piccache.cnki.net/kdn/KCMS/detail/resource/gb/css_min/Global.min.css?v=FBC16D09D6F9935E">
    <link rel="stylesheet" type="text/css" href="http://piccache.cnki.net/kdn/KCMS/detail/resource/gb/css_min/knetdetail.min.css?v=FBC16D09D6F9935E11231">
    <link rel="stylesheet" type="text/css" href="http://piccache.cnki.net/kdn/KCMS/detail/resource/gb/css/ecplogin.min.css?v=FBC16D09D6F9935E">
    <link rel="stylesheet" type="text/css" href="http://piccache.cnki.net/kdn/KCMS/detail/resource/gb/css_min/picModule.min.css?v=FBC16D09D6F9935E"><script type="text/javascript" src="/kcms/detail/js/getLink.aspx"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/resource/gb/js/min/rs.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/jquery-1.4.2.min.js"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/jquery.PrintArea.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/Common.min.js?v=FBC16D09D6F9935E1027"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/highcharts.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/json2.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/raphael.amd.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/CnkiFlashEmbed.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/jquery.mousewheel.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/NiceDCenter.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/Kajax.min.js?v=FBC16D09D6F9935E"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/CatalogFun.min.js?v=FBC16D09D6F9935E1027"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/detail.min.js?v=FBC16D09D6F9935E12"></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/recommendpic.min.js?v=FBC16D09D6F9935E"></script></head>
  <body><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/WideScreen.min.js"></script><input id="loginuserid" type="hidden" value="WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!"><input id="listv" type="hidden" value=""><input id="deliveryType" type="hidden" value=""><input id="deliveryUid" type="hidden" value=""><input id="deliveryUname" type="hidden" value=""><input id="deliveryCoutent" type="hidden" value="#"><input id="deliveryTable" type="hidden" value=""><input id="SingePointShow" type="hidden" value=""><script type="text/javascript" src="http://piccache.cnki.net/kdn/kns/script/jQuery-1.11.3.min.js"></script><script type="text/javascript" src="&#xA;        http://login.cnki.net/TopLogin/api/loginapi/get?type=top&amp;localCSS=&amp;returnurl=http%3a%2f%2fkns.cnki.net%2fKCMS%2fdetail%2fdetail.aspx%3fdbcode%3dCJFQ%26dbname%3dCJFD2009%26filename%3dRKYZ200902004%26uid%3dWEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0%3d%249A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!%26v%3dMTU2ODdTN0RoMVQzcVRyV00xRnJDVVJMMmVaZVptRmlIbFU3dklOeWJTZExHNEh0ak1yWTlGWUlSOGVYMUx1eFk%3d"></script><div id="headerBox"></div>
    <div class="line-box">
      <h1><span id="catalog_Ptitle"></span><span class="kcmslogo"></span></h1>
    </div><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/CnkiFlashEmbed.js?v=FBC16D09D6F9123&#xA;          "></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/jquery.mousewheel.js?v=FBC16D09D6F99123&#xA;          "></script><div id="mainArea" class="wxwrap">
      <div class="wxwrap">
        <div class="searchtop"><span class="showPlaceholder"><input id="searchinput" name="searchinput" type="text" onkeypress="setPlaceholder(this);" onpaste="return setPlaceholder(this);" onkeyup="setPlaceholder(this);"><label for="searchinput" class="placeholder" id="searchtext">��������������</label></span><input id="searchbtn" type="button" value="����" onclick="submitSearch()"></div>
      </div><script>      
      $("#searchinput").keypress(function (event) {
      if (event.keyCode == 13)
      submitSearch();
      });
    </script><script>$("#catalog_Ptitle").html("�ڿ�");</script><div class="wxside">
        <div id="CatalogSide" class="wxside kcmsCatalog">
          <div class="clHd">֪ʶ�ڵ�</div>
          <div class="clBd">
            <dl>
              <dt id="lcatalog_Ptitle" onclick="TurnToTitle('catalog_Ptitle')"><a><i></i>������Ϣ
              </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_ABSTRACT" onclick="TurnToTitle('catalog_ABSTRACT')"><a><i></i>ժҪ
                </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_KEYWORD" onclick="TurnToTitle('catalog_KEYWORD')"><a><i></i>�ؼ���
                </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_ZTCLS" onclick="TurnToTitle('catalog_ZTCLS')"><a><i></i>�����
                </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_divimg" class="leftBar_Img" style="display:none;" onclick="TurnToTitle('catalog_divimg')"><a><i></i>����ͼƬ
              </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_divzqcl" class="leftBar_Img" style="display:none;" onclick="TurnToTitle('catalog_divzqcl')"><a><i></i>��ǿ����
              </a></dt>
            </dl>
          </div>
          <div class="clHd">
      ֪ʶ����
      <input id="catalogIds" type="hidden" value=""></div>
          <div class="clBd">
            <dl>
              <dt id="lcatalog_ref" onclick="TurnToTitle('catalog_ref')"><a><i></i>��������
              </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_func601" onclick="GetAndShowFiles(this);"><a><i></i>��������
          </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_func604" onclick="GetAndShowFiles(this);"><a><i></i>��������
          </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_func605" onclick="GetAndShowFiles(this);"><a><i></i>�����Ƽ�
          </a></dt>
            </dl>
            <dl style="display:none;">
              <dt id="lcatalog_func602" onclick="GetAndShowFiles(this);"><a><i></i>����ָ��
          </a></dt>
            </dl>
            <dl>
              <dt id="lcatalog_func603" onclick="GetAndShowFiles(this);"><a><i></i>��ػ�������
              </a></dt>
            </dl>
          </div>
        </div>
      </div>
      <div class="wxmain">
        <div class="wxTitle">
          <h2 class="title">�ĸ￪�������й�������ᱣ���ƶȵķ�չ��Ｐ����˼��</h2><a class="btn-note" target="_blank" href="http://x.cnki.net/search/common/testlunbo?dbcode=CJFD&amp;tablename=CJFD2009&amp;filename=RKYZ200902004&amp;filesourcetype=1"><img src="resource/gb/images/note-btn.gif"></a><div class="author"><span><a onclick="&#xA;                    TurnPageToKnet('au','����Ⱥ','');&#xA;                  ">����Ⱥ</a></span></div>
          <div class="orgn"></div>
          <div class="link"><a class="icon icon-output" href="javascript:void(0);" onclick="&#xA;        SubTurnExport('http://kns.cnki.net/kns/ViewPage/viewsave.aspx','CJFD2009!RKYZ200902004!1!0')&#xA;      "><i></i>����/�ο�����
    </a><span id="AttentionYes" style="display:none;" class="followtop"><a class="icon icon-followSuccess" title="����ȥ �ҵĹ�ע �鿴����" target="mycnkitarget" href="http://kns.cnki.net/knsdelivery/mycnki.aspx?uid=WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&amp;type=2&#xA;                    "><i></i>�ѹ�ע       
      </a></span><span class="followtop" id="AttentionNo" style="position:relative;"><a class="icon icon-follow" title="��ע����" href="javascript:void(0);" onclick="AttentionServiceParam('2', 'WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!','CJFD2009','RKYZ200902004','0');"><i></i>��ע
      </a><div class="popflow" id="popupTips" style="display:none;">
                <div class="popflowArr"></div>
                <div class="popflowCot">
                  <div class="hd"><a href="javascript:void(0);" onclick="$('#popupTips').hide();$('#popupmsg').html('')" class="close">X</a></div>
                  <div class="bd">
                    <p class="mes" id="popupmsg" name="popupmsg">��ע�ɹ���</p>
                    <p class="des">
              �ӹ�ע������������� <a target="_mycnki" href="http://kns.cnki.net/knsdelivery/mycnki.aspx?uid=WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&amp;type=2">
                �ҵĹ�ע
              </a> �еõ������׵ı���Ƶ�α仯��֪ͨ��
            </p>
                  </div>
                  <div class="ft"><a class="extra" title="����" href="javascript:void(0);" onclick="SubScription('2', 'WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!', 'CJFD2009|');">
              �㻹����ͨ��������ʽ�õ�������Ϣ&gt;&gt;
            </a></div>
                </div>
              </div><script>
        AttentionServiceParam('2', 'WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!','CJFD2009','RKYZ200902004','1');
      </script></span><span class="shareBoard" onmouseover="$('#sharedet').show();$('#this').addClass('shareBoardCUR')" onmouseout="$('#sharedet').hide();$('#this').removeClass('shareBoardCUR')"><a class="icon icon-share" href="#"><i></i>����<em></em></a><script> document.write(ShareAstr('shareHide'));</script></span><a class="icon icon-favor" title="�ղ�" href="javascript:void(0);" onclick="AddFavTitle('')"><i></i>�ղ�
    </a><a class="icon icon-print" href="javascript:void(0);" onclick="window.print();"><i></i>��ӡ
    </a><a class="icon icon-comment" title="����" href="#" style="display:none;"><i></i>����
    </a><span class="otherversions" style="display:none"></span></div>
        </div>
        <div id="datapupart"></div>
        <div class="wxInfo">
          <div class="wxBaseinfo">
            <p><label id="catalog_ABSTRACT">ժҪ��</label><span id="ChDivSummary" name="ChDivSummary">������ᱣ���ƶȵı���Ϊ�ҹ��ĸ￪����������ƶȱ���һ����Ҫ���档����̽�����ҹ��������ϱ����ƶȵĸĸũ��������ϱ����ƶ����й��̼�����,�ع�������ȼú����긣������,ָ����Щ��ʩ���ڱ�֤��������˵Ļ���������Ҫ,ʵ������������Ŀ��,��Ӧ�˿����仯�Ŀ��ٷ�չ,ά������ȶ��ͼӿ���Ὠ��������Ҫ���á�����Ҳ���,������ᾭ�õĲ��Ϸ�չ,������ᱣ���ƶ��е�������Ҳ���ϱ�¶����,��Ҫ��չ�����о�����ʱ�������ߵ���,�������ҹ�������ᱣ����ҵ�ķ�չ,�ٽ�ȫ��С������ʵ�֡����Ļ����й��ĸ￪����������������ᱣ���ƶȵķ�չ�ĸ�Ч���ϸ��Է���������,ָ����ǰ���ڵ���Ҫ����,����������������εȽ�һ����չ�ĶԲ�˼����</span><span><a id="ChDivSummaryMore" onclick="MoerSummary('ChDivSummary','ChDivSummaryMore','ChDivSummaryReset')" style="display:none">����</a><a id="ChDivSummaryReset" onclick="ResetSummary('ChDivSummary','ChDivSummaryMore','ChDivSummaryReset')" style="display:none">��ԭ</a></span><br></p><script type="text/javascript">
      AbstractFilter('ChDivSummary','ChDivSummaryMore','ChDivSummaryReset');
    </script><p><label id="catalog_KEYWORD">�ؼ��ʣ�</label><a onclick="&#xA;                      TurnPageToKnet('kw','�ĸ￪��','')&#xA;                    ">�ĸ￪��;
                  </a><a onclick="&#xA;                      TurnPageToKnet('kw','������ᱣ��','')&#xA;                    ">������ᱣ��;
                  </a><a onclick="&#xA;                      TurnPageToKnet('kw','������ϱ���','')&#xA;                    ">������ϱ���;
                  </a></p>
            <p><label id="catalog_ZTCLS">����ţ�</label>F842.6</p>
            <p><label id="catalog_divimg" style="display:none ;">����ͼƬ��</label><div id="imgdiv" class="imgcont"></div>
            </p>
            <div id="zqfilelist"></div>
            <div class="dllink" id="DownLoadParts"><a onclick="WriteKrsDownLog()" target="_blank" class="icon icon-dlcaj" id="cajDown" name="cajDown" href="http://kns.cnki.net/kns/download.aspx?filename=klWZ0h2a1FUYzdkcxhnR3gnZZhnZ2YVc2QXMLN2UsZlWadHU5c2NrklbVdTaFpUSUNnSKxkVENFbRNnWYlleJVGOzpXSLZjem12NXlmZrZFdHNWTtZDSEFkQDhXY1kUOXhHbGlFUv0ERHZWYzZ1Y1NVM0pXSrNEb&amp;tablename=CJFD2009">
        CAJ����
      </a><a onclick="WriteKrsDownLog()" target="_blank" class="icon icon-dlpdf" id="pdfDown" name="pdfDown" href="http://kns.cnki.net/kns/download.aspx?filename=klWZ0h2a1FUYzdkcxhnR3gnZZhnZ2YVc2QXMLN2UsZlWadHU5c2NrklbVdTaFpUSUNnSKxkVENFbRNnWYlleJVGOzpXSLZjem12NXlmZrZFdHNWTtZDSEFkQDhXY1kUOXhHbGlFUv0ERHZWYzZ1Y1NVM0pXSrNEb&amp;tablename=CJFD2009&amp;dflag=pdfdown&#xA;              ">
        PDF����
      </a></div>
            <div class="dllink-down">
              <div class="info">
                <div class="total"><span class="a"><label>���أ�</label><b>2271</b></span><span class="h"><label>ҳ�룺</label><b>20-31</b></span><span class="h"><label>ҳ����</label><b>12</b></span><span class="h"><label>��С��</label><b>263K</b></span></div>
                <div class="hotspotCen" style="display:none;"><label>�ȵ��ע�ȣ�</label><div class="hotspot"><span value="" style="width:0%;" class="HotSpotPower"></span></div><span class="HotSpotValue" id="HotValue">0</span><b class="h">��ע��������ء����������ֵ��</b></div>
              </div>
              <div class="qr-code"><img alt="" src="http://app.cnki.net/Parts/QRCode/Get?source=KCMS&amp;text=http%3a%2f%2fm.cnki.net%2fcnkiday%2fappdownzwj.html%3ftype%3dCJFD%26id%3dRKYZ200902004"><p class="text"><b>�ֻ��Ķ�����</b><span>���ذ�װ�ֻ�APP</span><span>ɨ��ͬ���Ķ�����</span></p><i class="icon-trangle"></i><div class="tip-pop">
                  <div class="inner">
                    <h6>����ʹ���ֻ��Ķ�</h6>
                    <div class="f-left first"><img alt="" src="/kcms/Detail/resource/gb/images/icon-qrcode-download.jpg"><span>��һ��</span><p>ɨ���ά������</p>
                      <p>"�ƶ�֪��-ȫ��ѧ���챨"�ͻ���</p>
                    </div>
                    <div class="f-left second"><img alt="" src="/kcms/Detail/resource/gb/images/icon-pop-sample.jpg"><span>�ڶ���</span><p>�򿪡�ȫ��ѧ���챨��</p>
                      <p>�����ҳ���Ͻǵ�ɨ��ͼ��</p>
                    </div>
                    <div class="f-left third"><img alt="" src="http://app.cnki.net/Parts/QRCode/Get?source=KCMS&amp;text=http%3a%2f%2fm.cnki.net%2fcnkiday%2fappdownzwj.html%3ftype%3dCJFD%26id%3dRKYZ200902004"><span>������</span><p>ɨ���ά��</p>
                      <p>�ֻ�ͬ���Ķ���ƪ����</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="wxsour">
            <div class="cover"><a id="jpic" onclick="getKns55NaviLink('WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!','CJFQ','CJFQbaseinfo','RKYZ');"></a><i></i></div>
            <div class="sourinfo">
              <p class="title"><a onclick="getKns55NaviLink('WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!','CJFQ','CJFQbaseinfo','RKYZ');">�˿��о�</a></p>
              <p><a onclick="getKns55NaviLink('WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!','CJFQ','CJFQbaseinfo','RKYZ');">Population Research</a></p>
              <p><a onclick="getKns55NaviLinkIssue('WEEvREcwSlJHSldRa1FhcTdWZDhMQ0QxSjZrZ1p5WGsyazF1c0RsUm9lZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!','CJFQ','CJFQyearinfo','RKYZ','2009','02')">2009��02��
                </a></p>
              <p>
                  ISSN��1000-6087</p>
              <p>���ĺ����ڿ�</p><span id="bqsm"></span></div>
            <div class="sourlink"><span id="mlyll"></span><a target="_blank" class="icon icon-subm" href="&#xA;                  http://RKYZ.cbpt.cnki.net&#xA;                "><i></i>������Ͷ��
              </a><a target="_blank" class="icon icon-ediemail" href="&#xA;                  mailto:RKYZ@chinajournal.net.cn&#xA;                "><i></i>�༭������
              </a></div><script type="text/javascript">
                RegDujia('CJFQ','RKYZ','2009','02','jpic');
              </script></div>
        </div>
        <div class="wxMod" id="catalog_ref" style="display:none">
          <h2 id="MapTitle" class="hd hdTab"><a class="active" href="javascript:void(0)" onclick="showRefChart(this)">��������</a><a href="javascript:void(0)" onclick="showFlash(this)">�ο���֤ͼ��</a></h2>
        </div>
        <div class="wxMod" id="ref_nodata" style="display:none">
          <h3 class="title2">
        ��������
        <b class="titleTotle">δ�ҵ��������</b></h3>
        </div>
        <div id="MapArea" style="display:none">
          <div class="MapAreaLeft">
            <div class="map">
              <div class="jdwx" title="">�ڵ�����</div>
              <div class="gywx"><a id="rl5" name="rl" title="��Ҳ��ͬ�����ף��뱾������ͬ�ο����׵����ף��뱾���й�ͬ�о�����������">��������</a><span id="rc5">(0)</span></div>
              <div class="tbywx"><a id="rl6" name="rl" title="�뱾��ͬʱ����Ϊ�ο��������õ����ף��뱾�Ĺ�ͬ��Ϊ��һ���о��Ļ���">ͬ��������</a><span id="rc6">(0)</span></div>
              <div class="rjckwx"><a id="rl2" name="rl" title="���Ĳο����׵Ĳο����ס���һ����ӳ�����о������ı���������">�����ο�����</a><span id="rc2">(0)</span></div>
              <div class="ckwx"><a id="rl1" name="rl" title="��ӳ�����о������ı���������">�ο�����</a><span id="rc1">(0)</span></div>
              <div class="yzwx"><a id="rl3" name="rl" title="���ñ��ĵ����ס������о������ļ�����Ӧ�á���չ������">��֤����</a><span id="rc3">(0)</span></div>
              <div class="rjyzwx"><a id="rl4" name="rl" title="������֤���׵���֤���ס�����һ����ӳ�����о������ļ�������չ������">������֤����</a><span id="rc4">(0)</span></div>
            </div>
            <div class="time"><span onmouseover="TimeAxisMoveRight('AxisFrameDivLeft');" onmouseout="TimeAxisStop();" onclick="TimeAxisMoveFaster();" class="ArrowLeftDisable" title="��ʾǰ������" id="ArrowLeft_AxisFrameDivLeft"></span><div class="year" id="AxisFrameDivLeft"></div><span onmouseover="TimeAxisMoveLeft('AxisFrameDivLeft');" onmouseout="TimeAxisStop();" onclick="TimeAxisMoveFaster()" class="ArrowRightEnable" title="��ʾ��������" id="ArrowRight_AxisFrameDivLeft"></span><div class="TimeMiddle" id="AxisFrameDivCurrent" style="height: 55px;"></div><span onmouseover="TimeAxisMoveRight('AxisFrameDivRight');" onmouseout="TimeAxisStop();" onclick="TimeAxisMoveFaster()" class="ArrowLeftDisable" title="��ʾǰ������" id="ArrowLeft_AxisFrameDivRight"></span><div class="year" id="AxisFrameDivRight"></div><span onmouseover="TimeAxisMoveLeft('AxisFrameDivRight');" onmouseout="TimeAxisStop();" onclick="TimeAxisMoveFaster()" class="ArrowRightEnable" title="��ʾ��������" id="ArrowRight_AxisFrameDivRight"></span><span style="display: none; visibility: hidden;" class="ArrowLeftEnable" alt=""></span><div class="clear"></div>
            </div>
            <div id="NodeValueDiv1" class="TimeHide" onmouseout="HideNodeValueDiv();" onmouseover="window.clearTimeout(window.timeout_NodeValueDiv);">
              <ul>
                <li><a id="NodeValueDiv1ReferType1Link" onclick="ChangeReferType('1');" title="��ӳ�����о������ı���������">�ο�����</a><span id="NodeValueDiv1ReferType1Level1"></span></li>
                <li><a id="NodeValueDiv1ReferType2Link" onclick="ChangeReferType('2');" title="���Ĳο����׵Ĳο����ס���һ����ӳ�����о������ı���������">�����ο�����</a><span id="NodeValueDiv1ReferType2Level2"></span></li>
              </ul>
            </div>
            <div id="NodeValueDiv2" class="TimeHide" onmouseout="HideNodeValueDiv();" onmouseover="window.clearTimeout(window.timeout_NodeValueDiv);">
              <ul>
                <li><a id="NodeValueDiv2ReferType4Link" onclick="ChangeReferType('3');" title="���ñ��ĵ����ס������о������ļ�����Ӧ�á���չ������">��֤����</a><span id="NodeValueDiv2ReferType4Level1"></span></li>
                <li><a id="NodeValueDiv2ReferType16Link" onclick="ChangeReferType('4');" title="������֤���׵���֤���ס�����һ����ӳ�����о������ļ�������չ������">������֤����</a><span id="NodeValueDiv2ReferType16Level2"></span></li>
              </ul>
            </div>
            <div id="NodeValueDiv3" class="TimeHide" onmouseout="HideNodeValueDiv();" onmouseover="window.clearTimeout(window.timeout_NodeValueDiv);">
              <ul>
                <li><a id="NodeValueDiv3ReferType1Link" onclick="ChangeReferType('1');" title="��ӳ�����о������ı���������">�ο�����</a><span id="NodeValueDiv3ReferType1Level1"></span></li>
                <li><a id="NodeValueDiv3ReferType2Link" onclick="ChangeReferType('2');" title="���Ĳο����׵Ĳο����ס���һ����ӳ�����о������ı���������">�����ο�����</a><span id="NodeValueDiv3ReferType2Level2"></span></li>
                <li><a id="NodeValueDiv3ReferType4Link" onclick="ChangeReferType('3');" title="���ñ��ĵ����ס������о������ļ�����Ӧ�á���չ������">��֤����</a><span id="NodeValueDiv3ReferType4Level1"></span></li>
                <li><a id="NodeValueDiv3ReferType16Link" onclick="ChangeReferType('4');" title="������֤���׵���֤���ס�����һ����ӳ�����о������ļ�������չ������">������֤����</a><span id="NodeValueDiv3ReferType16Level2"></span></li>
              </ul>
            </div>
          </div>
        </div><script type="text/javascript">       
        SetRefChartDataEx('CJFQ','rkyz200902004','CJFD2009','2009');
      </script><iframe id="frame1" name="frame1" scrolling="no" height="0" frameborder="no" width="100%"></iframe>
        <div id="func607" class="wxMod"></div>
        <iframe id="framecatalog_CkFiles" name="framecatalog_CkFiles" width="100%" height="0" frameborder="no" scrolling="no" src=""></iframe>
        <iframe id="framecatalog_YzFiles" name="framecatalog_YzFiles" width="100%" height="0" frameborder="no" scrolling="no" src=""></iframe>
        <div id="func601" class="wxMod"></div>
        <div id="func614" class="wxMod"></div>
        <div id="func604" class="wxMod"></div>
        <div id="func605" class="wxMod"></div>
        <div id="func602" class="wxMod"></div>
        <div id="func603" class="wxMod"></div>
      </div>
    </div><script type="text/javascript">
      GetInfo('RKYZ','2009','02','�˿��о�');
      try{ GetImgPath('rkyz200902004');}catch(err){};

      
      function LoadFilesFromId(oid)
      {
      if(!oid) return;
      switch (oid)
      {
      case "catalog_func607":  
      WriteToPage('rkyz200902004','CJFD2009','CJFQ','CJFQ','607');
      
      LoadFile('framecatalog_CkFiles','/kcms/detail/frame/list.aspx?filename=rkyz200902004&dbcode=CJFQ&dbname=CJFD2009&reftype=1');
      
      LoadFile('framecatalog_YzFiles','/kcms/detail/frame/list.aspx?filename=rkyz200902004&dbcode=CJFQ&dbname=CJFD2009&reftype=3');
      
      break;
      case "catalog_func601":  
      WriteToPage('rkyz200902004','CJFD2009','CJFQ','CJFQ','601');
      break;
      case "catalog_func604":  
      WriteToPage('rkyz200902004','CJFD2009','CJFQ','CJFQ','604');
      break;
      case "catalog_func605":
      WriteToPage('rkyz200902004','CJFD2009','CJFQ','CJFQ','605');
      break;
      case "catalog_func602":
      WriteToPage('rkyz200902004','CJFD2009','CJFQ','CJFQ','602');
      break;
      case "catalog_func603":
      WriteToPage('rkyz200902004','CJFD2009','CJFQ','CJFQ','603');
      break;
      default : break;
      }
      }
      
      setYxCatalog();

    </script><div class="wxToolbar" id="wxDlToolbar">
      <div class="wxwrap">
        <div class="dllink"><a onclick="WriteKrsDownLog()" target="_blank" class="icon icon-dlcaj" id="cajDownF" name="cajDown" href="/kns/download.aspx?filename=klWZ0h2a1FUYzdkcxhnR3gnZZhnZ2YVc2QXMLN2UsZlWadHU5c2NrklbVdTaFpUSUNnSKxkVENFbRNnWYlleJVGOzpXSLZjem12NXlmZrZFdHNWTtZDSEFkQDhXY1kUOXhHbGlFUv0ERHZWYzZ1Y1NVM0pXSrNEb&amp;tablename=CJFD2009">
              CAJ����
            </a><a onclick="WriteKrsDownLog()" target="_blank" class="icon icon-dlpdf" id="pdfDownF" name="pdfDown" href="/kns/download.aspx?filename=klWZ0h2a1FUYzdkcxhnR3gnZZhnZ2YVc2QXMLN2UsZlWadHU5c2NrklbVdTaFpUSUNnSKxkVENFbRNnWYlleJVGOzpXSLZjem12NXlmZrZFdHNWTtZDSEFkQDhXY1kUOXhHbGlFUv0ERHZWYzZ1Y1NVM0pXSrNEb&amp;tablename=CJFD2009&amp;dflag=pdfdown">
              PDF����
            </a></div>
        <div class="infotxt">
          <div class="total"><span class="a"><label>���أ�</label><b>2271</b></span><span class="h"><label>ҳ�룺</label><b>20-31</b></span><span class="h"><label>ҳ����</label><b>12</b></span><span class="h"><label>��С��</label><b>263K</b></span></div>
          <div class="hotspotCen" style="display:none;"><label>�ȵ��ע�ȣ�</label><div class="hotspot"><span value="" style="width:0%;" class="HotSpotPower"></span></div><span class="HotSpotValue" id="HotValue">0</span><b class="h">��ע��������ء����������ֵ��</b></div>
        </div>
      </div>
    </div><script>FloatDownloadPartCantrol();</script><iframe scrolling="no" frameborder="0" id="headad" style="display:none;"></iframe>
    <div class="wait" id="waitDiv" style="visibility:hidden;">
          ����Ϊ�����ң����Ե�...
        </div>
    <div id="footerBox"></div>
    <div class="fixedbar">
      <div class="adviceside"><a class="fixCon" target="_blank" href="http://help.cnki.net/">������ѯ</a><a target="_blank" class="fixFed" href="http://kns.cnki.net/knsvote/vote.aspx">
          �û�����
        </a></div>
      <div class="backtop hiddenV" id="backtop"><a id="backTopSide" href="javascript:scroll(0,0);" title="���ض���"></a></div>
    </div><script type="text/javascript" src="http://kns.cnki.net/KRS/Scripts/Recommend.js"></script><script> toTop();</script><script>
      InsertCatalog();

      try{
        FlushLogin();
        modifyEcpHeader(true);
      }
      catch(es){}
      
      KLogin.getFooter();
    </script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/klib.min.js?v=20171013&#xA;              "></script><script type="text/javascript" src="http://piccache.cnki.net/kdn/KCMS/detail/js/min/Timeaxis.min.js?v=20171013&#xA;              "></script><script type="text/javascript">LoadScript('http://piccache.cnki.net/kdn/KCMS/detail/js/min/cnkisug.min.js',function(){sugPara.IsTopK = false; sugPara.IsExp = false; sugPara.IsAttr = false;InitSug('http://acad3.cnki.net');});</script><script>
          setRecommendPic();
        </script></body>
</html>'''
def jiexiwangye(head,tail,s):
    ph=s.find(head)
    pt=s.find(tail,ph)
    s1=s[ph+len(head):pt]
    return s1
l=[]
head0='''<h2 class="title">'''
tail0='''</h2><a class="btn-note" target="_blank"'''
head1='''TurnPageToKnet('au','''
tail1=''');&#xA;'''
#head2='''TurnPageToKnet('in','''
#tail2=''')&#xA;'''
head3='''name="ChDivSummary">'''
tail3='''</span><span><a'''
head4='''GetInfo('''
tail4=''');'''
head=[head0,head1,head3,head4]
tail=[tail0,tail1,tail3,tail4]
i=0
while i<len(head):
    ss=jiexiwangye(head[i],tail[i],s)
    l.append(ss)
    i+=1
print(l)


