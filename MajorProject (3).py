<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g#scrollTo=_b6FaVv7HrHs -->
<html lang="en" theme="dark" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="mbr8004@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./MajorProject (3)_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-fhF6HYISoYLkhpTlAJBpytq+eKnHbn4KQovxIc2m9B3MH/43tMbFUbSUDANMK7jX" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./MajorProject (3)_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-fhF6HYISoYLkhpTlAJBpytq+eKnHbn4KQovxIc2m9B3MH/43tMbFUbSUDANMK7jX" nonce=""></script><script type="text/javascript" async="" src="./MajorProject (3)_files/js" nonce=""></script><script src="./MajorProject (3)_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./MajorProject (3)_files/cb=gapi.loaded_0" nonce="" async=""></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>MajorProject (3).ipynb - Colab</title><link href="./MajorProject (3)_files/css2" rel="stylesheet"><link href="./MajorProject (3)_files/css" rel="stylesheet"><script nonce="">
      window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
    </script><script async="" src="./MajorProject (3)_files/analytics.js.download" nonce=""></script><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_yb{font:13px/27px Roboto,Arial,sans-serif;z-index:986}.gb_R{display:none}.gb_Q{background-size:32px 32px;border:0;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_kb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_kb.gb_Q{height:30px;width:30px}.gb_kb.gb_Q:hover,.gb_kb.gb_Q:active{box-shadow:none}.gb_lb{background:#fff;border:none;border-radius:50%;bottom:2px;box-shadow:0px 1px 2px 0px rgba(60,64,67,0.3),0px 1px 3px 1px rgba(60,64,67,0.15);height:14px;margin:2px;position:absolute;right:0;width:14px;line-height:normal;z-index:1}.gb_mb{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25),(min-resolution:1.25dppx){.gb_Q::before,.gb_nb::before{display:inline-block;-webkit-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:left 0;transform-origin:left 0}.gb_4 .gb_nb::before{-webkit-transform:scale(scale(.416666667));transform:scale(scale(.416666667))}}.gb_Q:hover,.gb_Q:focus{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Q:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_Q:active::after{background:rgba(0,0,0,.1);border-radius:50%;content:"";display:block;height:100%}.gb_ob{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_ob{width:auto}.gb_ob:hover,.gb_ob:focus{opacity:.85}.gb_pb .gb_ob,.gb_pb .gb_qb{line-height:26px}#gb#gb.gb_pb a.gb_ob,.gb_pb .gb_qb{font-size:11px;height:auto}.gb_rb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_0a:hover .gb_rb{opacity:.85}.gb_Xa>.gb_z{padding:3px 3px 3px 4px}.gb_sb.gb_jb{color:#fff}.gb_2 .gb_ob,.gb_2 .gb_rb{opacity:1}#gb#gb.gb_2.gb_2 a.gb_ob,#gb#gb .gb_2.gb_2 a.gb_ob{color:#fff}.gb_2.gb_2 .gb_rb{border-top-color:#fff;opacity:1}.gb_la .gb_Q:hover,.gb_2 .gb_Q:hover,.gb_la .gb_Q:focus,.gb_2 .gb_Q:focus{box-shadow:0 1px 0 rgba(0,0,0,0.15),0 1px 2px rgba(0,0,0,0.2)}.gb_tb .gb_z,.gb_ub .gb_z{position:absolute;right:1px}.gb_z.gb_1,.gb_vb.gb_1,.gb_0a.gb_1{-webkit-box-flex:0;-webkit-flex:0 1 auto;flex:0 1 auto}.gb_wb.gb_xb .gb_ob{width:30px!important}.gb_P{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_yb .gb_P,.gb_zb .gb_P{right:0;top:0}.gb_Ha a.gb_Va{border-radius:100px;background:#0b57d0;background:var(--gm3-sys-color-primary,#0b57d0);box-sizing:border-box;color:#fff;color:var(--gm3-sys-color-on-primary,#fff);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_Ha a.gb_Wa{border-radius:100px;border:1px solid;border-color:#747775;border-color:var(--gm3-sys-color-outline,#747775);background:none;box-sizing:border-box;color:#0b57d0;color:var(--gm3-sys-color-primary,#0b57d0);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_1a.gb_H a.gb_Va,.gb_2a.gb_H a.gb_Va,.gb_3a.gb_H a.gb_Va{background:#c2e7ff;background:var(--gm3-sys-color-secondary-fixed,#c2e7ff);color:#001d35;color:var(--gm3-sys-color-on-secondary-fixed,#001d35)}.gb_Ha.gb_H a.gb_Wa{color:#a8c7fa;color:var(--gm3-sys-color-primary,#a8c7fa)}.gb_Ha a.gb_Od{padding:10px 12px;margin:12px 16px 12px 10px;min-width:85px}@media (max-width:640px){.gb_Ha a.gb_Od{min-width:75px}}.gb_Ha,.gb_Dd{font-family:"Google Sans Text",Roboto,Helvetica,Arial,sans-serif;font-style:normal}.gb_Ha.gb_1a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a.gb_Pd{background:#fff;background:var(--og-bar-background,var(--gm3-sys-color-background,#fff))}.gb_Ha.gb_1a .gb_pd.gb_qd,.gb_Ha.gb_1a a.gb_Z,.gb_Ha.gb_1a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a .gb_rd .gb_Qd,.gb_Ha.gb_1a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}@media (forced-colors:active) and (prefers-color-scheme:dark){.gb_Ha svg,.gb_Ha.gb_1a svg,.gb_Ha.gb_H svg{color:white}}.gb_Ha.gb_H.gb_1a{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a.gb_Pd{background:transparent}.gb_Ha.gb_H.gb_1a .gb_pd.gb_qd,.gb_Ha.gb_H.gb_1a a.gb_Z,.gb_Ha.gb_H.gb_1a span.gb_Z{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a .gb_rd .gb_Qd,.gb_Ha.gb_H.gb_1a .gb_id .gb_Qd{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ha.gb_H.gb_1a.gb_Pd{background:#1f1f1f;background:var(--og-bar-background,var(--gm3-sys-color-background,#131314))}.gb_Ha.gb_2a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a.gb_Pd{background:#e9eef6;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#e9eef6))}.gb_Ha.gb_2a .gb_pd.gb_qd,.gb_Ha.gb_2a a.gb_Z,.gb_Ha.gb_2a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a .gb_rd .gb_Qd,.gb_Ha.gb_2a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ha.gb_H.gb_2a{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a.gb_Pd{background:#282a2c;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#282a2c))}.gb_Ha.gb_H.gb_2a .gb_pd.gb_qd,.gb_Ha.gb_H.gb_2a a.gb_Z,.gb_Ha.gb_H.gb_2a span.gb_Z{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a .gb_rd .gb_Qd,.gb_Ha.gb_H.gb_2a .gb_id .gb_Qd{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ha.gb_3a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a.gb_Pd{background:transparent}.gb_Ha.gb_3a .gb_pd.gb_qd,.gb_Ha.gb_3a a.gb_Z,.gb_Ha.gb_3a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a .gb_rd .gb_Qd,.gb_Ha.gb_3a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ha.gb_3a.gb_H.gb_Pd{background:transparent}.gb_Ha.gb_3a.gb_H .gb_pd.gb_qd,.gb_Ha.gb_3a.gb_H a.gb_Z,.gb_Ha.gb_3a.gb_H span.gb_Z{color:white;color:var(--og-theme-color,white)}.gb_Ha.gb_3a.gb_H .gb_rd .gb_Qd,.gb_Ha.gb_3a.gb_H .gb_id .gb_Qd{color:white;color:var(--og-theme-color,white)}.gb_Ha.gb_3a.gb_H svg{color:white;color:var(--og-theme-color,white)}.gb_Ha a.gb_Z,.gb_Ha span.gb_Z{text-decoration:none}.gb_pd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-box-flex:1;-webkit-flex:1 1 auto;flex:1 1 auto}.gb_ud{display:none}.gb_Ha.gb_9a .gb_pd{margin-bottom:0}.gb_rd.gb_sd .gb_pd{padding-left:4px}.gb_Ha.gb_9a .gb_td{position:relative;top:-2px}.gb_Ha{min-width:160px;position:relative}.gb_Ha.gb_ad{min-width:120px}.gb_Ha.gb_Rd .gb_Sd{display:none}.gb_Ha.gb_Rd .gb_Kd{height:56px}header.gb_Ha{display:block}.gb_Ha svg{fill:currentColor}.gb_Td{position:fixed;top:0;width:100%}.gb_Ud{box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Vd{height:64px}.gb_Kd{box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ha:not(.gb_9a) .gb_Kd{padding:8px}.gb_Ha:not(.gb_9a) .gb_Kd a.gb_Wd{margin:12px 8px 12px 10px}.gb_Ha.gb_Xd .gb_Kd{-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha .gb_Kd.gb_Ld.gb_Zd{min-width:0}.gb_Ha.gb_9a .gb_Kd{padding:4px;padding-left:8px;min-width:0}.gb_Ha.gb_9a .gb_Kd a.gb_Wd{margin:12px 8px 12px 10px}.gb_Sd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none;user-select:none}.gb_0d>.gb_Sd{display:table-cell;width:100%}.gb_rd{padding-right:25px;box-sizing:border-box;-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha.gb_9a .gb_rd{padding-right:14px}.gb_1d{-webkit-box-flex:1;-webkit-flex:1 1 100%;flex:1 1 100%}.gb_1d>:only-child{display:inline-block}.gb_2d.gb_jd{padding-left:4px}.gb_2d.gb_3d,.gb_Ha.gb_Xd .gb_2d,.gb_Ha.gb_9a:not(.gb_Dd) .gb_2d{padding-left:0}.gb_Ha.gb_9a .gb_2d.gb_3d{padding-right:0}.gb_Ha.gb_9a .gb_2d.gb_3d .gb_Xa{margin-left:10px}.gb_jd{display:inline}.gb_Ha.gb_dd .gb_2d.gb_4d,.gb_Ha.gb_Dd .gb_2d.gb_4d{padding-left:2px}.gb_pd{display:inline-block}.gb_2d{box-sizing:border-box;height:48px;padding:0 4px;padding-left:5px;-webkit-box-flex:0;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Dd{height:48px}.gb_Ha.gb_Dd{min-width:auto}.gb_Dd .gb_2d{float:right;padding-left:32px;padding-left:var(--og-bar-parts-side-padding,32px)}.gb_Dd .gb_2d.gb_5d{padding-left:0}.gb_6d{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text;user-select:text}.gb_a a,.gb_6c a{color:inherit}.gb_qd{text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.gb_qd{opacity:1}.gb_7d{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}.gb_0{display:inline-block;padding-left:15px}.gb_0 .gb_Z{display:inline-block;line-height:24px;vertical-align:middle}.gb_8d{text-align:left}.gb_K{display:none}@media screen and (max-width:319px){.gb_Kd .gb_J{display:none;visibility:hidden}}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}.gb_S{display:none!important}.gb_jb{visibility:hidden}@media screen and (max-width:319px){.gb_Kd:not(.gb_Ld) .gb_J{display:none;visibility:hidden}}.gb_vd{display:inline-block;vertical-align:middle}.gb_wd .gb_R{bottom:-3px;right:-5px}@if (RTL_LANG){.gb_wd .gb_R{left:-5px}}.gb_vd:first-child{padding-left:0}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:50%;box-sizing:border-box;height:40px;width:40px}.gb_B,#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}x:-o-prefocus{border-bottom-color:#ccc}.gb_ma{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:0;top:54px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text;user-select:text}.gb_vd.gb_5a .gb_ma,.gb_5a.gb_ma{display:block}.gb_Ad{position:absolute;right:0;top:54px;z-index:-1}.gb_pb .gb_ma{margin-top:-10px}.gb_vd:first-child{padding-left:4px}.gb_Ha.gb_Bd .gb_vd:first-child{padding-left:0}.gb_Cd{position:relative}.gb_id .gb_Cd,.gb_Dd .gb_Cd{float:right}.gb_B{padding:8px;cursor:pointer}.gb_Fd button svg,.gb_B{border-radius:50%}.gb_vd{padding:4px}.gb_Ha.gb_Bd .gb_vd{padding:4px 2px}.gb_Ha.gb_Bd .gb_z.gb_vd{padding-left:6px}.gb_ma{z-index:991;line-height:normal}.gb_ma.gb_Id{left:0;right:auto}@media (max-width:350px){.gb_ma.gb_Id{left:0}}.gb_Jd .gb_ma{top:56px}.gb_z .gb_B{padding:4px}.gb_T{display:none}.gb_0a:not(.gb_Wd){position:relative}.gb_be::after{content:"";border:1px solid #202124;opacity:.13;position:absolute;top:4px;left:4px;border-radius:50%;width:30px;height:30px;box-sizing:content-box}.gb_Xa{box-sizing:border-box;cursor:pointer;display:inline-block;height:48px;overflow:hidden;outline:none;padding:7px 0 0 16px;vertical-align:middle;width:142px;border-radius:28px;background-color:transparent;border:1px solid;position:relative}.gb_Xa .gb_0a{width:32px;height:32px;padding:0}.gb_Xa .gb_R{bottom:-2px;right:-4px}.gb_1a .gb_Xa,.gb_2a .gb_Xa{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_1a.gb_H .gb_Xa,.gb_2a.gb_H .gb_Xa{border-color:#8e918f;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#8e918f))}.gb_3a .gb_Xa{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_3a.gb_H .gb_Xa{border-color:#e3e3e3;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_4a{display:inherit}.gb_Xa .gb_4a{background:#fff;border-radius:6px;display:inline-block;left:15px;position:static;padding:2px;top:-1px;height:32px;box-sizing:border-box;width:78px}.gb_6a{text-align:center}.gb_6a.gb_7a{background-color:#f1f3f4}.gb_6a .gb_8a{vertical-align:middle;max-height:28px;max-width:74px}.gb_Ha .gb_Xa .gb_z.gb_vd{padding:0;margin-right:9px;float:right}.gb_Ha:not(.gb_9a) .gb_Xa{margin-left:10px;margin-right:4px}.gb_Xa .gb_be::after{left:0;top:0}@media screen and (max-width:480px){.gb_Xa .gb_4a{display:none}.gb_Xa{border:none;border-radius:50%;height:40px;margin:4px;outline:1px solid transparent;padding:0;width:40px}.gb_Ha .gb_Xa .gb_z.gb_vd{padding:4px;margin-right:0}}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.cPj2G-PDsqg.2019.O","co.in","en","425",0,[4,2,"","","","884150452","0"],null,"6Pe8aeG_J8Wo6-AP6dGmoQk",null,0,"og.qtm.vjyYcS7rQwo.L.W.O","AA2YrTvL7TWoIS7jW_IXNVd6orqvk8gC_A","AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","mbr8004@gmail.com","","ADUjzeHSovZswxO9K9Uh0C3RZwlWhX4Hzbq2Nk_vKR9IqJezcCh5CZrqD1sFTHb8N__9Fl3dLd1qpnd4D5zbJVYHmkfqMNVeOA",0,0,null,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.5G9F9JPGjf8.O/d=1/rs=AHpOoo-OYuAVGK84U6cg5lkjGc85qYpeMw/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20260309.0_p0","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en","884150452.0",8,null,1,0,null,null,null,null,"3700949,105109531,105109534,105140909,105140912,115517798,115517801,116249040,116249043",null,null,null,"6Pe8aeG_J8Wo6-AP6dGmoQk",0,0,0,null,2,5,"nn",75,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.cPj2G-PDsqg.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTvL7TWoIS7jW_IXNVd6orqvk8gC_A"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.vjyYcS7rQwo.L.W.O/m=qcwid,qba,d_b_gm3,d_wi_gm3,d_lo_gm3/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?baea=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",null,1,1,0,0,"Account alert",0],null,1,null,1,1,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,null,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g\u0026timeStmp=1773991912\u0026secTok=.AG5fkS_hEkCoHf85bBgUJ_cafiv-eKtiJw\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,null,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g\u0026ec=GAZAqQM",null,null,0,null,null,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,null,null,0,null,0,0,"1184720131",3,1,0,0],0,null,null,null,1,0,"mbr8004@gmail.com",0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Fa,Ga,Za,bb,db,ib,eb,kb,qb,Db,Eb,Fb,Gb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Dk=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Ea=function(a,b){return b===void 0?a.j!==Da&&!!(2&(a.ha[_.v]|0)):!!(2&b)&&a.j!==Da};Fa=function(a){return a};Ga=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ha=function(a){a=Error(a);Ga(a,"warning");return a};_.Ja=function(a,b){if(a!=null){var c;var d=(c=Ia)!=null?c:Ia={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ga(a,"incident"),_.ka(a))}};
_.La=function(a){if(typeof a!=="boolean")throw Error("k`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Oa=function(a){if(!(0,_.Na)(a))throw _.Ha("enum");return a|0};_.Pa=function(a){if(typeof a!=="number")throw _.Ha("int32");if(!(0,_.Na)(a))throw _.Ha("int32");return a|0};_.Qa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Ra=function(a){return a==null||typeof a==="string"?a:void 0};
_.Ua=function(a,b,c){if(a!=null&&a[_.Sa]===_.Ta)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Xa=function(a){const b=_.Va(_.Wa);return b?a[b]:void 0};Za=function(a,b){b<100||_.Ja(Ya,1)};
bb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Va(_.Wa),g;!e&&f&&(g=a[f])&&g.Ad(Za);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=$a)!=null?r:Fa)(g-p,p,a,k,void 0)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const E=r-p;var q=void 0;((q=b)!=null?q:b={})[E]=w}else f[r]=w}if(k)for(let w in k){q=
k[w];if(q==null||(q=c(q,d))==null)continue;h=+w;let E;if(m&&!Number.isNaN(h)&&(E=h+p)<g)f[E]=q;else{let O;((O=b)!=null?O:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Va(_.Wa)&&(a=_.Xa(a))&&"function"==typeof _.ab&&a instanceof _.ab&&(f[_.Wa]=a.i());return f};
db=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.cb)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:bb(a,b,db)}if(a!=null&&a[_.Sa]===_.Ta)return eb(a);if("function"==typeof _.fb&&a instanceof _.fb)return a.j();return}return a};ib=function(a,b){if(b){$a=b==null||b===Fa||b[gb]!==hb?Fa:b;try{return eb(a)}finally{$a=void 0}}return eb(a)};
eb=function(a){a=a.ha;return bb(a,a[_.v]|0,db)};
_.lb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("l");e=a[_.v]|0;if(jb&&1&e)throw Error("m");2048&e&&!(2&e)&&kb();if(e&256)throw Error("n");if(e&64)return(e|d)!==e&&(a[_.v]=e|d),a;if(c&&(e|=128,c!==a[0]))throw Error("o");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("q");for(var h in k)if(f=+h,f<g)c[f+
b]=k[h],delete k[h];else break;e=e&-16760833|(g&1023)<<14;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("r");e=e&-16760833|(h&1023)<<14}}}a[_.v]=e|64|d;return a};kb=function(){if(jb)throw Error("p");_.Ja(mb,5)};
qb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.nb(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Sa]===_.Ta)return b=a.ha,c=b[_.v]|0,_.Ea(a,c)?a:_.ob(a,b,c)?_.pb(a,b):_.nb(b,c);if("function"==typeof _.fb&&a instanceof _.fb)return a};_.pb=function(a,b,c){a=new a.constructor(b);c&&(a.j=Da);a.o=Da;return a};
_.nb=function(a,b,c,d){d!=null||(d=!!(34&b));a=bb(a,b,qb,d);d=32;c&&(d|=2);b=b&16769217|d;a[_.v]=b;return a};_.rb=function(a){const b=a.ha,c=b[_.v]|0;return _.Ea(a,c)?_.ob(a,b,c)?_.pb(a,b,!0):new a.constructor(_.nb(b,c,!1)):a};_.sb=function(a){if(a.j!==Da)return!1;var b=a.ha;b=_.nb(b,b[_.v]|0);b[_.v]|=2048;a.ha=b;a.j=void 0;a.o=void 0;return!0};_.tb=function(a){if(!_.sb(a)&&_.Ea(a,a.ha[_.v]|0))throw Error();};_.ub=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.ob=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.j=Da,!0):!1};_.wb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>14&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.yb=function(a,b,c,d,e){let f=!1;d=_.xb(a,d,e,g=>{const h=_.Ua(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ea(d)&&_.ub(a,b),d};_.zb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(){this.qa=this.qa;this.Y=this.Y};_.Ab=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Bb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Cb=function(a){for(const b in a)return!1;return!0};
Db=Object.defineProperty;Eb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Fb=Eb(this);Gb=function(a,b){if(b)a:{var c=Fb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Db(c,a,{configurable:!0,writable:!0,value:b})}};
Gb("globalThis",function(a){return a||Fb});Gb("Symbol.dispose",function(a){return a?a:Symbol("b")});var Jb,Kb,Nb;_.Hb=_.Hb||{};_.t=this||self;Jb=function(a,b){var c=_.Ib("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Kb=_.t._F_toggles_gbar_||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Lb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Mb="closure_uid_"+(Math.random()*1E9>>>0);
Nb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Nb;return _.z.apply(null,arguments)};_.Ob=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Va=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.vk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Pb=!!(Kb[0]>>20&1),Qb=!!(Kb[0]>>15&1),Rb=!!(Kb[0]>>22&1),Sb=!!(Kb[0]&1024);var na=Pb?Rb:Jb(610401301,!1),jb=Pb?Qb||!Sb:Jb(748402147,!0);_.Tb=_.ba(a=>a!==null&&a!==void 0);var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Wb,Ub,Xb,Vb;_.cb=_.ba(a=>fa?a>=Ub&&a<=Vb:a[0]==="-"?ja(a,Wb):ja(a,Xb));Wb=Number.MIN_SAFE_INTEGER.toString();Ub=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Xb=Number.MAX_SAFE_INTEGER.toString();Vb=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Yb=typeof TextDecoder!=="undefined";_.Zb=typeof TextEncoder!=="undefined";var oa,$b=_.t.navigator;oa=$b?$b.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.ac=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.bc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.cc=function(a){_.cc[" "](a);return a};_.cc[" "]=function(){};var qc;_.dc=_.ra();_.ec=_.sa();_.fc=_.u("Edge");_.hc=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.ic=_.ma()&&!_.u("Edge");_.jc=_.za();_.kc=wa()?oa.platform==="Windows":_.u("Windows");_.lc=wa()?oa.platform==="Android":_.u("Android");_.mc=xa();_.nc=_.u("iPad");_.oc=_.u("iPod");_.pc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.hc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.fc)return/Edge\/([\d\.]+)/.exec(c);if(_.ec)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.ic)return/WebKit\/(\S+)/.exec(c);if(_.dc)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.ec){var rc;const c=_.t.document;rc=c?c.documentMode:void 0;if(rc!=null&&rc>parseFloat(a)){qc=String(rc);break a}}qc=a}_.sc=qc;_.tc=_.ta();_.uc=xa()||_.u("iPod");_.vc=_.u("iPad");_.wc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.xc=ua();_.yc=_.va()&&!_.ya();var Ya,mb,gb;_.Wa=_.Ca();_.zc=_.Ca();Ya=_.Ca();_.Ac=_.Ca();mb=_.Ca();_.Sa=_.Ca("m_m",!0);gb=_.Ca();_.Bc=_.Ca();var Dc;_.v=_.Ca("jas",!0);Dc=[];Dc[_.v]=7;_.Cc=Object.freeze(Dc);var Da;_.Ta={};Da={};_.Ec=Object.freeze({});var hb={};var Ia=void 0;_.Fc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Gc=Number.isSafeInteger;_.Na=Number.isFinite;_.Hc=Math.trunc;var $a;_.Ic=_.ia(0);_.Jc={};_.Kc=function(a,b,c,d,e){b=_.xb(a.ha,b,c,e);if(b!==null||d&&a.o!==Da)return b};_.xb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Lc=function(a,b,c,d){_.tb(a);const e=a.ha;_.wb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.ha,f=e[_.v]|0;b=_.yb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ea(a,f)){const g=_.rb(b);g!==b&&(_.sb(a)&&(e=a.ha,f=e[_.v]|0),b=g,f=_.wb(e,f,c,b,d),_.ub(e,f))}return b};_.D=function(a,b,c){c==null&&(c=void 0);_.Lc(a,b,c);c&&!_.Ea(c)&&_.ub(a.ha);return a};_.F=function(a,b,c=!1,d){let e;return(e=_.Ma(_.Kc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Ra(_.Kc(a,b,d)))!=null?e:c};_.H=function(a,b,c){return _.Ra(_.Kc(a,b,c,_.Jc))};
_.J=function(a,b,c,d){return _.Lc(a,b,c==null?c:_.La(c),d)};_.K=function(a,b,c){return _.Lc(a,b,c==null?c:_.Pa(c))};_.L=function(a,b,c,d){return _.Lc(a,b,_.Qa(c),d)};_.M=function(a,b,c,d){return _.Lc(a,b,c==null?c:_.Oa(c),d)};_.N=class{constructor(a,b,c){this.ha=_.lb(a,b,c,2048)}toJSON(){return ib(this)}wa(a){return JSON.stringify(ib(this,a))}};_.N.prototype[_.Sa]=_.Ta;_.N.prototype.toString=function(){return this.ha.toString()};_.Mc=_.zb();_.Nc=_.zb();_.Oc=_.zb();_.Pc=Symbol();var Qc=class extends _.N{constructor(a){super(a)}};_.Sc=class extends _.N{constructor(a){super(a)}D(a){return _.K(this,3,a)}};_.Tc=class extends _.N{constructor(a){super(a)}};_.x.prototype.qa=!1;_.x.prototype.isDisposed=function(){return this.qa};_.x.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.x.prototype[Symbol.dispose]=function(){this.dispose()};_.x.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Uc=class extends _.x{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}yb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].yb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Wc=class extends _.x{constructor(){var a=_.Vc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Xc=class extends _.N{constructor(a){super(a)}};var Yc=class extends _.N{constructor(a){super(a)}};var ad;_.Zc=function(a,b,c=98,d=new _.Sc){if(a.i){const e=new Qc;_.L(e,1,b.message);_.L(e,2,b.stack);_.K(e,3,b.lineNumber);_.M(e,5,1);_.D(d,40,e);a.i.log(c,d)}};ad=class{constructor(){var a=$c;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Sc){_.Zc(this,a,98,c)}};var bd,cd;bd=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.ac(c,b,a)}catch(d){console.error(d)}}}};_.dd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new cd(a,b,c));bd(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.i=a;bd(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.j=a;bd(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
cd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.ed=a=>{var b="uc";if(a.uc&&a.hasOwnProperty(b))return a.uc;b=new a;return a.uc=b};_.P=class{constructor(){this.v=new _.dd;this.i=new _.dd;this.D=new _.dd;this.B=new _.dd;this.C=new _.dd;this.A=new _.dd;this.o=new _.dd;this.j=new _.dd;this.F=new _.dd;this.G=new _.dd}K(){return this.v}qa(){return this.i}O(){return this.D}M(){return this.B}P(){return this.C}L(){return this.A}Y(){return this.o}J(){return this.j}N(){return this.F}static i(){return _.ed(_.P)}};var hd;_.gd=function(){return _.C(_.fd,_.Tc,5)};hd=class extends _.N{constructor(a){super(a)}};var id;window.gbar_&&window.gbar_.CONFIG?id=window.gbar_.CONFIG[0]||{}:id=[];_.fd=new hd(id);var $c;$c=_.C(_.fd,Yc,3)||new Yc;_.Vc=new ad;_.A("gbar_._DumpException",function(a){_.Vc?_.Vc.log(a):console.error(a)});_.jd=new Wc;var ld;_.md=function(a,b){var c=_.kd.i();if(a in c.i){if(c.i[a]!=b)throw new ld;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Cb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.kd=class{constructor(){this.i={};this.j={}}static i(){return _.ed(_.kd)}};_.nd=class extends _.aa{constructor(){super()}};ld=class extends _.nd{};_.A("gbar.A",_.dd);_.dd.prototype.aa=_.dd.prototype.then;_.A("gbar.B",_.P);_.P.prototype.ba=_.P.prototype.qa;_.P.prototype.bb=_.P.prototype.O;_.P.prototype.bd=_.P.prototype.P;_.P.prototype.bf=_.P.prototype.K;_.P.prototype.bg=_.P.prototype.M;_.P.prototype.bh=_.P.prototype.L;_.P.prototype.bj=_.P.prototype.Y;_.P.prototype.bk=_.P.prototype.J;_.P.prototype.bl=_.P.prototype.N;_.A("gbar.a",_.P.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var od=new Uc;_.md("api",od);
var pd=_.gd()||new _.Tc,qd=window,rd=_.y(_.H(pd,8));qd.__PVT=rd;_.md("eq",_.jd);
}catch(e){_._DumpException(e)}
try{
_.sd=class extends _.N{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var td=class extends _.N{constructor(a){super(a)}};var ud=class extends _.x{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.H(a,1));_.Ma(_.Kc(a,12))!=null&&(d.dpo=_.Ab(_.F(a,12)));d.ms=_.y(_.H(a,2));d.m=_.y(_.H(a,3));d.l=[];_.G(b,1)&&(a=_.H(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.H(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var vd=_.C(_.fd,_.Xc,14);if(vd){var wd=_.C(_.fd,_.sd,9)||new _.sd,xd=new td,yd=new ud;yd.init(vd,wd,xd);_.md("gs",yd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_mbr8004@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./MajorProject (3)_files/bundle.css"><script nonce="">var colabVersionTag = 'colab-external_20260318-060049_RC00_885490043'; var colabScsVersion = '7e817d0baee282a55a901c82e75da009'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_prompt_cell\x22: true, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_service_client_type\x22: \x22\x22, \x22ai_user_input_char_limit\x22: 100000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_subpaths_in_kernel_url\x22: true, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22assign_ping_hostname\x22: \x22https:\/\/ping.prod.colab.dev\x22, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22, \x22*.proxy.googlers.com\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_autocomplete\x22: false, \x22composer_client_events_context\x22: true, \x22composer_compaction_interval\x22: 0, \x22composer_compaction_overlap_size\x22: 0, \x22composer_context_max_variable_length\x22: 500000, \x22composer_custom_context\x22: false, \x22composer_default_dock_right\x22: true, \x22composer_early_stopping_for_image_truncation\x22: false, \x22composer_focused_cell_context\x22: true, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: true, \x22composer_generated_cell_placement_logic\x22: true, \x22composer_kernel_files_in_context\x22: true, \x22composer_model_strategy\x22: 0, \x22composer_replace_empty_cells_when_adding_new_cells\x22: false, \x22composer_show_debug_info\x22: false, \x22composer_show_single_diff_buttons\x22: false, \x22composer_suggestion_chips_in_chat\x22: false, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: true, \x22connect_enterprise_vm\x22: true, \x22converse_notebook_context_length\x22: 40000, \x22critique_comments\x22: false, \x22data_inspector\x22: true, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecated_accelerator_models\x22: \x5b\x22V28\x22\x5d, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_agent_pending_markdown_network_requests\x22: false, \x22drop_chat_links\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22edu_promotion_banner\x22: false, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_bigquery_data_explorer\x22: false, \x22enable_colab_mcp_integration\x22: true, \x22enable_colab_mcp_showdiff\x22: false, \x22enable_composer_changeset_plan_stacking\x22: true, \x22enable_composer_code_report\x22: false, \x22enable_composer_fp_orcas_integration\x22: false, \x22enable_composer_fp_orcas_integration_v2\x22: false, \x22enable_composer_g_4_g_models\x22: true, \x22enable_composer_generated_cell_insertion_position\x22: false, \x22enable_composer_suggestion_chips\x22: true, \x22enable_composer_text_cell_transformations\x22: true, \x22enable_dsa_agent_steps_bundle\x22: false, \x22enable_fp_user_provided_context_links\x22: false, \x22enable_g_4_g_as_default_model\x22: true, \x22enable_gcp_preferences\x22: false, \x22enable_iframe_unloading\x22: true, \x22enable_improved_composer_context_mentions\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_prism_mode\x22: false, \x22enable_rt_on_create\x22: false, \x22enable_vscode_telemetry\x22: true, \x22enable_web_mcp\x22: false, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jspb_analytics\x22: true, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: true, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22migrate_assignments\x22: true, \x22migrate_ccu_info\x22: true, \x22migrate_delete_assignment\x22: false, \x22migrate_tfe_keep_alive\x22: true, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: false, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22oneplatform_api_key\x22: \x22AIzaSyA2BvntLwNwFthUB4w6_Bhn0cMlVHwyaHc\x22, \x22oneplatform_endpoint\x22: \x22https:\/\/colab.clients6.google.com\x22, \x22optimize_composer_context_order\x22: false, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22pds_minting\x22: false, \x22preference_deep_equality_check\x22: true, \x22prereq_cells_next_steps\x22: true, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_composer_planning_overeagerness\x22: false, \x22refresh_warning_timeout_ms\x22: 604800000, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr_skip_fallback\x22: true, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: false, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222026.01\x22, \x222025.10\x22, \x222025.07\x22\x5d, \x22server_execution_queue\x22: true, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22snippets_ui_refresh\x22: false, \x22sql_cell\x22: false, \x22sql_completion_lsp\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_timeout_ms\x22: 300000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22trim_filename_extension\x22: false, \x22truncate_composer_execution_results\x22: true, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_kernel_state_metadata_adk\x22: false, \x22use_kkb_if_configured\x22: false, \x22use_refactored_constraints\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22G4\x22, \x22H100\x22, \x22L4\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_composer_tools\x22: \x5b\x5d, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22vscode_test_feature\x22: \x22prod\x22, \x22want_completions_ai_consent_campaign\x22: true, \x22ids\x22: \x5b20730460, 20730652, 20730656, 20730547, 20730556, 20730559, 20730183, 20730457, 20730640\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_service_client_type\x22: 45723040, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22assign_ping_hostname\x22: 45747049, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_autocomplete\x22: 45718105, \x22composer_client_events_context\x22: 45729342, \x22composer_compaction_interval\x22: 45749782, \x22composer_compaction_overlap_size\x22: 45749781, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_custom_context\x22: 45728743, \x22composer_default_dock_right\x22: 45755037, \x22composer_early_stopping_for_image_truncation\x22: 45719141, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_generated_cell_placement_logic\x22: 45721730, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_replace_empty_cells_when_adding_new_cells\x22: 45788233, \x22composer_show_debug_info\x22: 45700003, \x22composer_show_single_diff_buttons\x22: 45723066, \x22composer_suggestion_chips_in_chat\x22: 45757782, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22connect_enterprise_vm\x22: 45730782, \x22converse_notebook_context_length\x22: 45705427, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecated_accelerator_models\x22: 45724327, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_agent_pending_markdown_network_requests\x22: 45768013, \x22drop_chat_links\x22: 45646864, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22edu_promotion_banner\x22: 45740730, \x22embedded_use_websockets\x22: 45691694, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_bigquery_data_explorer\x22: 45765771, \x22enable_colab_mcp_integration\x22: 45741279, \x22enable_colab_mcp_showdiff\x22: 45768032, \x22enable_composer_changeset_plan_stacking\x22: 45744296, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_fp_orcas_integration\x22: 45744285, \x22enable_composer_fp_orcas_integration_v2\x22: 45758361, \x22enable_composer_g_4_g_models\x22: 45745479, \x22enable_composer_generated_cell_insertion_position\x22: 45763491, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_composer_text_cell_transformations\x22: 45758370, \x22enable_dsa_agent_steps_bundle\x22: 45755666, \x22enable_fp_user_provided_context_links\x22: 45746774, \x22enable_g_4_g_as_default_model\x22: 45745683, \x22enable_gcp_preferences\x22: 45762481, \x22enable_iframe_unloading\x22: 45765934, \x22enable_improved_composer_context_mentions\x22: 45721452, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_prism_mode\x22: 45765531, \x22enable_rt_on_create\x22: 45667583, \x22enable_vscode_telemetry\x22: 45760437, \x22enable_web_mcp\x22: 45769687, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22migrate_assignments\x22: 45752830, \x22migrate_ccu_info\x22: 45716751, \x22migrate_delete_assignment\x22: 45760675, \x22migrate_tfe_keep_alive\x22: 45766773, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22oneplatform_api_key\x22: 45717742, \x22oneplatform_endpoint\x22: 45717924, \x22optimize_composer_context_order\x22: 45759155, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22pds_minting\x22: 45648255, \x22preference_deep_equality_check\x22: 45740961, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_composer_planning_overeagerness\x22: 45758628, \x22refresh_warning_timeout_ms\x22: 45765093, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22server_execution_queue\x22: 45425600, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22snippets_ui_refresh\x22: 45737461, \x22sql_cell\x22: 45425497, \x22sql_completion_lsp\x22: 45688254, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22trim_filename_extension\x22: 45691676, \x22truncate_composer_execution_results\x22: 45746694, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_kernel_state_metadata_adk\x22: 45737477, \x22use_kkb_if_configured\x22: 45733350, \x22use_refactored_constraints\x22: 45740233, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_composer_tools\x22: 45752901, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22vscode_test_feature\x22: 45755614, \x22want_completions_ai_consent_campaign\x22: 45671138\x7d\x7d'); var colabUserEmail = 'mbr8004@gmail.com'; var colabRenderDataToken = 'AFWLbD3BNb9vyPc1vdgnLGWG6kDlPD-0tsY19IK3zzC4Y2oxVyNACyagh_qChKNyD0G_mDV3uzu6XIaIf6tYtE_D6EZPoCn4UBLTIgRZlsZ8lce_'; var colabConfig = '\x5b\x5b\x22mbr8004@gmail.com\x22,\x5b1,\x22AHXL0D0lfbh3Z94QSbCoAsEx\/EAnzDtBo3OFCBadQ\/wDhY\/sXo8OQL6x8bm8nZ+ICERv6wsYPhjQBvSDpAM3xIityLta4OKhKNfM6fnfzYhAhM1fVu037jsHDzr1nrOfHamDkg2OhXlmhOvG2ovQb8BYp2AQ8CKdOytfRuOO9cURG6n1b1Hutei0AeJMDxzTkbsEla6ndI\/TGdjfMYvLfvviU99WQT3vhE5QrA8kJRxMZwduw1h23QTDCDgy7IfENK7rA8hLfUll7BusSdHi\/KQIel\/OE9PWZ5bYrIllhJ+rrDttBSevQAUZ\/JsE97p4G59wRrrYC5zJh8Eq353pl+r0rRHf7zZQDZsBF10s3y3NbnphG5bdYRRJdb1GNik2nFm2C30eFlK9eoK4slurVk27oa9Qt4nVcvNEs32\/NUZ2RGsGuylatV+qdVFBVZvxx8Y3lXh1KHRPw7IpEBjZn0+XHcb8rIwVRDJlYtSMma1djbo7vA1hK4ZGTVVC90zb7ri2M8vXlmW3nDa65UX0O8y8rommzWYyyrTh509WBE+Z0uR2GSy4eHrNb6ZzocLcpDihZJ5UfXAJLYqqANdC8ee6Y+AR7sAZvAJcZ2h5weJ\/hmPL5GhzyXZiYCbKsDw+rhqR6DhTqfCYJjoKwG2AhJzRwIuWVWvuH4wITL4iStcRvduZVG6AqjqwcGWFuSXoBk2VzWhznDoAAVBIn9HqsCr+5cOW5aoWT+HsnL1icawQYDI2tESCof3QMFSDvsh02k0Iqe3qrTToU9QwG57NDw54mNv0EGez8oTb2hUDwrOKLsCWPJudDq\/RzGG9JkWSseFWMELU1JpLENpOzvjCI47nYCnrgVONXx3brgKhHdX3DfNJUEgkPZFgJ82TE1V3HDcjpIbRwJ3EgjKzgSrkwzJ7mgB6W3JbHjTDozPNY42xIONnh6PhWwnSkKuq1t68e6C5aTCz35RF7K8R4ELseK7d+o8gM5jiM7uQ3oeN6aXvSzSyFwSZGtdE8TR0RnTuXt7Zt\/d30Z87LDXEWJ8KlA+bL8rERn62o9wDBev92MnpaqNxc+T+0V2HAaXuxxIIFm2Zo51+dJMBhbTjBl+Yrw0c32lMmYN45tC6tJIMDLiqu8LLngsdwHM0aPaheOfJaxuyLXHEIFD81phYHm42xDaL1sM1tEWhG6\/IIqRbdfWN+Rb6H8MhWexzR6Yzjk0SjFayvn6BYVF6hgAGC2mClu4Hm9+eobOdDSQH67ZuhzuN0EPrvkPlDpPFETix6R8t7P+zy8cuQkxIipAIIApP0Tep8qIdURaZeEal8HbUtKPNo29NvnzkZMmdV5Q0rH6d+aIf95U1BgdNIx2c3bpfL9L4nUhtB49Ht5dpIffxzpkfmpgAby3do08xTcreR67x7ZhinT2fvBL8YlddzKf7SumhaWFcjsk6K9gTzbrRIY58maEBzanGcbUFq7Qu5EDE1\/qItGHYrjG0jJBlbYyP4MCSmeAY12\/zGZ5IS5qql\/i9tyA\/fiReJ65Qf\/c2Kmke9Ad+XBev9Dy\/M3lnLq+5iXiSqYbB2aDwszqK8RGdzMMb\/Gsp7fqchKs4A3POWzXGAzFZO3uKHCSBujr6aEIxvqgBKFAqhcY5kZSaNmvtYZFKp13S+WG2XqGuWeV9WFuK9fc5HzEQ5EsQWtmpcIklSu7GSvg967aRc21dU09PEs88uXQk+cjL3vfnYEqjo4gvZffNwlobyrHsQ5o9r7UWAq4XYLz59M79X9NlioZSdK72PE51I+uo30g6+bim2YZ0ZxU+cVDkvBe3YoZvhdlItFHP3YCaZuNGyLP1IwZ7200Qs7KCoOP6U8Ut99ujG4Bs6KsSwSFdm5ZiH7gECuUM1hggT35N6Fvn034s8fWPRKA4vzyN9ul\/k4SoO0u4wR4DW99IX8YYNu4iz5IET85AAWzquqd+\/eXKEGRTBASBFHuLaK+tMeHISnjxScqbXHJBKpINTv10OpGf\x22,\x22AJ9oCCxR4xZYZhpzruvGo3RyYxmiXcWyCCddvaMulzar7XWH2n1H11JyCFEiLLtJ+dh4BDOYtx3PeZK1pnu018QNZuf3DWHQDFgQ3L28kvQZaphnJ5+Ggwh4oFhCjk0m05mWHxnGKkck\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22,0,0,0\x5d,\x5b1,4,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/7e817d0baee282a55a901c82e75da009/img%2Ffavicon.ico"><meta name="google-site-verification" content="h4AyILcMXlXf3PDJKg3Fu2_dyS3jfH5im5G__oDgjOs"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="gl3hNNVi7GnXImkDiRAkUxkhUD4g7Ke8L4D6Ve8FEVY"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="HwWGKCyRK7kxGyAlA30sbbTly9VW0SOM7Sh4juqiOVA"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./MajorProject (3)_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./MajorProject (3)_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./MajorProject (3)_files/rs=AA2YrTvL7TWoIS7jW_IXNVd6orqvk8gC_A" nonce=""></script><link type="text/css" href="./MajorProject (3)_files/rs=AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww" rel="stylesheet"><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./MajorProject (3)_files/editor.main.css"><script async="async" type="text/javascript" src="./MajorProject (3)_files/editor.main.nls.js.download"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script src="./MajorProject (3)_files/api.js.download" nonce=""></script><script src="./MajorProject (3)_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #282a2c; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #282a2c;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #282a2c;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: #234521;
--vscode-diffEditor-removedTextBackground: #5b2022;
--vscode-diffEditor-insertedLineBackground: #22331f;
--vscode-diffEditor-removedLineBackground: #3c1a1a;
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #282a2c;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #282a2c;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #282a2c;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #282a2c; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #82b76c; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #69a5d7; }
.mtk11 { color: #f28b82; }
.mtk12 { color: #d7ba7d; }
.mtk13 { color: #d49d87; }
.mtk14 { color: #dcdcdc; }
.mtk15 { color: #808080; }
.mtk16 { color: #4ec9b0; }
.mtk17 { color: #dcdcaa; }
.mtk18 { color: #f44747; }
.mtk19 { color: #82c6ff; }
.mtk20 { color: #c99cc6; }
.mtk21 { color: #c586c0; }
.mtk22 { color: #a79873; }
.mtk23 { color: #dd6a6f; }
.mtk24 { color: #5bb498; }
.mtk25 { color: #909090; }
.mtk26 { color: #778899; }
.mtk27 { color: #ff00ff; }
.mtk28 { color: #b46695; }
.mtk29 { color: #ff0000; }
.mtk30 { color: #4f76ac; }
.mtk31 { color: #3dc9b0; }
.mtk32 { color: #74b0df; }
.mtk33 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="" style="overscroll-behavior: contain; overflow: hidden;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;" inert="" aria-hidden="true"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;" inert="" aria-hidden="true"></div><div class="scripts" inert="" aria-hidden="true"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./MajorProject (3)_files/gapi_loader.js.download" nonce=""></script><script src="./MajorProject (3)_files/socketio_binary.js.download" nonce=""></script><script src="./MajorProject (3)_files/MathJax.js.download" nonce=""></script><script src="./MajorProject (3)_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./MajorProject (3)_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area" inert="" aria-hidden="true"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$091463802$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$091463802$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup" inert="" aria-hidden="true"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$091463802$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$091463802$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable="" inert="" aria-hidden="true"></div><div class="gb_T" ng-non-bindable="" inert="" aria-hidden="true"><div class="gb_Rc"><div>Google Account</div><div class="gb_g">Marthala Bhargavi</div><div>mbr8004@gmail.com</div><div class="gb_Sc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Jd;Jd=class extends _.nd{};_.Kd=function(a,b){if(b in a.i)return a.i[b];throw new Jd;};_.Ld=function(a){return _.Kd(_.kd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Od;_.Md=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Od=function(a){return new _.Nd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Pd=globalThis.trustedTypes;_.Qd=class{constructor(a){this.i=a}toString(){return this.i}};_.Rd=new _.Qd("about:invalid#zClosurez");_.Nd=class{constructor(a){this.Vh=a}};_.Sd=[Od("data"),Od("http"),Od("https"),Od("mailto"),Od("ftp"),new _.Nd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Td=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Ud=new _.Td(_.Pd?_.Pd.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Zd,ke,ne,Yd,$d,ee;_.Vd=function(a){return a==null?a:(0,_.Na)(a)?a|0:void 0};_.Wd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Na)(a)?a|0:void 0};_.Xd=function(a,b){return a.lastIndexOf(b,0)==0};Zd=function(){let a=null;if(!Yd)return a;try{const b=c=>c;a=Yd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.ae=function(){$d===void 0&&($d=Zd());return $d};
_.ce=function(a){const b=_.ae();a=b?b.createScriptURL(a):a;return new _.be(a)};_.de=function(a){if(a instanceof _.be)return a.i;throw Error("x");};_.fe=function(a){if(ee.test(a))return a};_.ge=function(a){if(a instanceof _.Qd)if(a instanceof _.Qd)a=a.i;else throw Error("x");else a=_.fe(a);return a};_.he=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};
_.ie=function(a,b,c,d){return _.Vd(_.Kc(a,b,c,d))};_.Q=function(a,b,c){return _.Ma(_.Kc(a,b,c,_.Jc))};_.je=function(a,b){return _.Wd(_.Kc(a,b,void 0,_.Jc))};ke=class extends _.N{constructor(a){super(a)}Yb(a){return _.L(this,24,a)}};_.le=function(){return _.C(_.fd,ke,1)};_.me=function(a){var b=_.Ka(a);return b=="array"||b=="object"&&typeof a.length=="number"};Yd=_.Pd;_.be=class{constructor(a){this.i=a}toString(){return this.i+""}};ee=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var te,xe,oe;_.qe=function(a){return a?new oe(_.pe(a)):ne||(ne=new oe)};_.re=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.S=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.se(c,"*",a,b)[0]||null);return a||null};_.se=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.ue=function(a,b){_.Bb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:te.hasOwnProperty(d)?a.setAttribute(te[d],c):_.Xd(d,"aria-")||_.Xd(d,"data-")?a.setAttribute(d,c):a[d]=c})};te={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.ve=function(a){return a?a.defaultView:window};_.ye=function(a,b){const c=b[1],d=_.we(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.ue(d,c));b.length>2&&xe(a,d,b);return d};xe=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.me(f)||_.Lb(f)&&f.nodeType>0?d(f):_.ac(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Md(f):f,d)}};
_.ze=function(a){return _.we(document,a)};_.we=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.Ae=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.Be=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.Ce=function(a,b){return a&&b?a==b||a.contains(b):!1};_.pe=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};oe=function(a){this.i=a||_.t.document||document};_.n=oe.prototype;
_.n.H=function(a){return _.re(this.i,a)};_.n.Ra=function(a,b,c){return _.ye(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.Pe=_.Ae;_.n.tg=_.Be;_.n.rg=_.Ce;
}catch(e){_._DumpException(e)}
try{
_.Mi=function(a){const b=_.he("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Oi=function(a){if(!a)return null;a=_.H(a,4);var b;a===null||a===void 0?b=null:b=_.ce(a);return b};_.Pi=function(a,b,c){a=a.ha;return _.yb(a,a[_.v]|0,b,c)!==void 0};_.Qi=class extends _.N{constructor(a){super(a)}};_.Ri=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Ti=function(a,b,c){a<b?Si(a+1,b):_.Vc.log(Error("W`"+a+"`"+b),{url:c})},Si=function(a,b){if(Ui){const c=_.ze("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.de(Ui);_.Mi(c);c.onerror=_.Ob(Ti,a,b,c.src);_.Ri("HEAD")[0].appendChild(c)}},Vi=class extends _.N{constructor(a){super(a)}};var Wi=_.C(_.fd,Vi,17)||new Vi,Xi,Ui=(Xi=_.C(Wi,_.Qi,1))?_.Oi(Xi):null,Yi,Zi=(Yi=_.C(Wi,_.Qi,2))?_.Oi(Yi):null,$i=function(){Si(1,2);if(Zi){const a=_.ze("LINK");a.setAttribute("type","text/css");a.href=_.de(Zi).toString();a.rel="stylesheet";let b=_.he("style",document);b&&a.setAttribute("nonce",b);_.Ri("HEAD")[0].appendChild(a)}};(function(){const a=_.le();if(_.Q(a,18))$i();else{const b=_.je(a,19)||0;window.addEventListener("load",()=>{window.setTimeout($i,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;" inert="" aria-hidden="true"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./MajorProject (3)_files/RotateCookiesPage.html" style="display: none;" inert="" aria-hidden="true" tabindex="-1"></iframe><div class="notebook-vertical" style="position: relative;" inert="" aria-hidden="true">
      <!--?lit$091463802$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><a id="link" class="button" href="https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g#notebook-main" tabindex="-1"><!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </a>
    </template><!--?lit$091463802$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$091463802$-->
    <!--?lit$091463802$-->
          <div id="private-outputs-warning" hidden="" class="header-warning private-outputs-warning"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$091463802$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip" tabindex="-1">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$091463802$--> <!--?lit$091463802$-->
    <div hidden="" class="header-warning refresh-warning undismissible"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
      <div class="message"><!--?lit$091463802$-->Your Colab version is out of date, please refresh to get the latest updates.</div>
      <div class="actions">
        <md-text-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <!--?lit$091463802$-->Refresh to update
        </md-text-button>
      </div>
    </div>
  
    <!--?lit$091463802$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><div id="header-logo">
              <!--?lit$091463802$--><!--?lit$091463802$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive" tabindex="-1">
        <!--?lit$091463802$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$--><svg viewBox="0 0 24 24"><!--?lit$091463802$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$091463802$--><!--?lit$091463802$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" tabindex="-1" style="width: 186.219px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">MajorProject (3).ipynb_</colab-input-sizer>
            <!--?lit$091463802$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$091463802$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" style="user-select: none;"><!--?lit$091463802$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$091463802$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$091463802$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$091463802$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$091463802$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$091463802$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$091463802$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$091463802$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$091463802$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$091463802$-->
      <!--?lit$091463802$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$091463802$--><md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$091463802$--><md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$091463802$--><md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Share notebook" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->people</md-icon>
                <!--?lit$091463802$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" hidden="" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Toggle Gemini" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
            <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
            <!--?lit$091463802$-->Gemini
          </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ha gb_Dd gb_yb gb_e gb_3a gb_dd" id="gb"><div class="gb_2d gb_wb gb_Sd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Cd" style="display:block"><div class="gb_jd"></div><div class="gb_z gb_vd gb_Qf gb_1"><div class="gb_D gb_vb gb_Qf gb_1"><a class="gb_B gb_0a gb_1" aria-expanded="false" aria-label="Google Account: Marthala Bhargavi  
(mbr8004@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/drive/1Ksma6siGK-uDjasndsHvtI4HPFQl8d7g&amp;ec=GBRAqQM" tabindex="-1" role="button"><span class="gb_be"><img class="gb_Q gbii" src="./MajorProject (3)_files/unnamed.png" srcset="https://lh3.google.com/u/0/ogw/AF2bZyhrLkPNxLPuXH_9ONNtRHTMYdnhKmhZOYYLpp0OQt58pQ=s32-c-mo 1x, https://lh3.google.com/u/0/ogw/AF2bZyhrLkPNxLPuXH_9ONNtRHTMYdnhKmhZOYYLpp0OQt58pQ=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></span><div class="gb_R gb_S" aria-hidden="true"><svg class="gb_La" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_Ma" cx="7" cy="7" r="7"></circle><path class="gb_Oa" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.zd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.zd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("t`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Ad=document.querySelector(".gb_J .gb_B"),Bd=document.querySelector("#gb.gb_ad");Ad&&!Bd&&_.zd(_.jd,Ad,"click");
}catch(e){_._DumpException(e)}
try{
_.nh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ka()&&a.i[b].B())return a.i[b];return null};_.oh=function(a,b){a.i[b.J()]=b};var ph=new class extends _.x{constructor(){var a=_.Vc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.nh(this)&&_.nh(this).J()==a||this.i[a].P(!0))}Ua(a){this.j=a;for(const b in this.i)this.i[b].ka()&&this.i[b].Ua(a)}oc(a){return a in this.i?this.i[a]:null}};_.md("dd",ph);
}catch(e){_._DumpException(e)}
try{
_.Gi=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Hi=document.querySelector(".gb_z .gb_B"),Ii=document.querySelector("#gb.gb_ad");Hi&&!Ii&&_.zd(_.jd,Hi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$091463802$-->
    <!--?lit$091463802$--><colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
        <!--?lit$091463802$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$091463802$--><span class="screenreader-only"><!--?lit$091463802$-->Show command palette <!--?lit$091463802$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$091463802$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
          <!--?lit$091463802$-->Commands
        </colab-toolbar-button>
    <!--?lit$091463802$--><span class="toolbar-add-code-split"><colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code" class=" split-button "><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
        <!--?lit$091463802$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$091463802$--><span class="screenreader-only"><!--?lit$091463802$-->Insert code cell below <!--?lit$091463802$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$091463802$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
              <!--?lit$091463802$-->Code
            </colab-toolbar-button>
            <!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" id="top-toolbar-add-code-dropdown-button" data-aria-label="Insert code cell options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert code cell options" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="top-toolbar-add-code-dropdown-button" message="Insert code cell options"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Insert code cell options</div><!----><!--?--></template>
    </colab-tooltip-trigger></span>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
        <!--?lit$091463802$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$091463802$--><span class="screenreader-only"><!--?lit$091463802$-->Add text cell <!--?lit$091463802$--></span>
      </md-text-button>
      <!--?lit$091463802$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$091463802$-->Text
          </colab-toolbar-button>
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button class="split-button" icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
        <!--?lit$091463802$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$091463802$--><span class="screenreader-only"><!--?lit$091463802$-->Run all cells in notebook <!--?lit$091463802$--></span>
      </md-text-button>
      <!--?lit$091463802$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$091463802$-->Run all
      </colab-toolbar-button>
      <!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$091463802$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$091463802$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$091463802$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$091463802$--><!----><md-menu-item command="restart" md-menu-item="" disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item disabled"><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true" disabled=""><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" md-menu-item="" disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item disabled"><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true" disabled=""><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-menu-item command="runafter" md-menu-item=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   "><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Run focused cell and all cells below</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" md-menu-item="" disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item disabled"><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true" disabled=""><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   "><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$091463802$-->
    <!--?lit$091463802$-->
    <!--?lit$091463802$-->
    <!--?lit$091463802$-->
    <!--?lit$091463802$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$091463802$-->
    <!--?lit$091463802$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$091463802$--><!--?--></template></colab-connect-warning-button>
    <!--?lit$091463802$--><!--?lit$091463802$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$091463802$--> <!--?lit$091463802$--><!--?-->
      <colab-toolbar-button id="connect" class="split-button" tooltipid="colab-connect-tooltip" tooltiptext="Click to connect"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
        <!--?lit$091463802$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$091463802$--><span class="screenreader-only"><!--?lit$091463802$-->Click to connect <!--?lit$091463802$--></span>
      </md-text-button>
      <!--?lit$091463802$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Click to connect" shortcut=""><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Click to connect</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$091463802$-->Reconnect
      </colab-toolbar-button>
      <!--?lit$091463802$--> <md-icon-button id="connect-dropdown" class="connect-dropdown" touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$091463802$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$091463802$-->
    <span class="collapsed-options">
      <!--?lit$091463802$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$091463802$-->
      <span class="colab-separator"></span>
    </span>
    <!--?lit$091463802$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" touch-target="none" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$091463802$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$091463802$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$091463802$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$091463802$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$091463802$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$091463802$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->code</md-icon>
    </md-icon-button> <!--?lit$091463802$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$091463802$--><md-icon-button toggle="" command="show-data-inspector" data-aria-label="Data inspector" title="Data inspector" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Data inspector" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->eye_tracking</md-icon>
    </md-icon-button> <!--?lit$091463802$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$091463802$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$091463802$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$091463802$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->folder</md-icon>
    </md-icon-button> <!--?lit$091463802$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$091463802$--><md-icon-button toggle="" command="show-data-explorer" data-aria-label="Data explorer" title="Data explorer" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Data explorer" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->table</md-icon>
    </md-icon-button> <!--?lit$091463802$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$091463802$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$091463802$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-QHZpOxZPKH2P" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$091463802$--><div class="indicator"></div>
      </div>
      <!--?lit$091463802$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$091463802$--><div class="colab-tab-title">
      <!--?lit$091463802$-->
      <span id="tab-title-QHZpOxZPKH2P"><!--?lit$091463802$--><!--?lit$091463802$-->Notebook<!--?--></span>
    </div> <!--?lit$091463802$--> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"><!----><!--?lit$091463802$--><!--?--></div>
      <!--?lit$091463802$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-0-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button id="tab-pane-0-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-scroller role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$091463802$-->
              <div class="notebook-content ">
                <!--?lit$091463802$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code notebook-cell code-has-output" id="cell-4FuiA0Cd7dK5" role="region" aria-label="Cell 0: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;google.colab&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;files</span></span><br><span><span class="mtk1">files.upload</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 73px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./MajorProject (3)_files/outputframe.html" class="" style="height: 73px;" tabindex="-1"></iframe></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell" id="cell-RLGxdMKs8mtI" role="region" aria-label="Cell 1: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk19">!</span><span class="mtk1">mkdir&nbsp;-p&nbsp;~/</span><span class="mtk14">.</span><span class="mtk1">kaggle</span></span><br><span><span class="mtk19">!</span><span class="mtk1">cp&nbsp;kaggle</span><span class="mtk14">.</span><span class="mtk1">json&nbsp;~/</span><span class="mtk14">.</span><span class="mtk1">kaggle/</span></span><br><span><span class="mtk19">!</span><span class="mtk1">chmod&nbsp;</span><span class="mtk6">600</span><span class="mtk1">&nbsp;~/</span><span class="mtk14">.</span><span class="mtk1">kaggle/kaggle</span><span class="mtk14">.</span><span class="mtk1">json</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 1 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-my5nBGNe8xOJ" role="region" aria-label="Cell 2: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk19">!</span><span class="mtk1">kaggle&nbsp;datasets&nbsp;download&nbsp;-d&nbsp;abdulhasibuddin/plant-</span><span class="mtk1">doc-dataset</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Dataset URL: <a rel="nofollow" target="_blank" href="https://www.kaggle.com/datasets/abdulhasibuddin/plant-doc-dataset" tabindex="-1">https://www.kaggle.com/datasets/abdulhasibuddin/plant-doc-dataset</a>
License(s): unknown
Downloading plant-doc-dataset.zip to /content
100% 880M/882M [00:10&lt;00:00, 45.1MB/s]
100% 882M/882M [00:10&lt;00:00, 85.7MB/s]
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-7Qw_EQRT88ur" role="region" aria-label="Cell 3: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="62" data-mode-id="notebook-python" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/6" style="width: 1722px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 1722px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1716px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1716px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1716px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1716px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">!</span><span class="mtk1">unzip&nbsp;plant-doc-dataset</span><span class="mtk14">.</span><span class="mtk1">zip</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1702px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1702px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="29" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1722px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="-1" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1722px;"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1920px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 1136.52px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 3 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Archive:  plant-doc-dataset.zip
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (10).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Apple Scab Leaf/Apple Scab Leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Apple leaf/Apple leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (10).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Apple rust leaf/Apple rust leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (1).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (2).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (3).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (4).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (5).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (6).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (7).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (8).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf spot/Bell_pepper leaf spot (9).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Bell_pepper leaf/Bell_pepper leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (10).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (11).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Blueberry leaf/Blueberry leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (10).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Cherry leaf/Cherry leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Corn Gray leaf spot/Corn Gray leaf spot (1).jpg  
  inflating: PlantDoc-Dataset/test/Corn Gray leaf spot/Corn Gray leaf spot (2).jpg  
  inflating: PlantDoc-Dataset/test/Corn Gray leaf spot/Corn Gray leaf spot (3).jpg  
  inflating: PlantDoc-Dataset/test/Corn Gray leaf spot/Corn Gray leaf spot (4).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (1).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (10).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (11).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (12).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (2).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (3).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (4).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (5).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (6).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (7).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (8).jpg  
  inflating: PlantDoc-Dataset/test/Corn leaf blight/Corn leaf blight (9).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (10).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Corn rust leaf/Corn rust leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Peach leaf/Peach leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (1).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (2).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (3).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (4).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (5).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (6).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (7).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf early blight/Potato leaf early blight (8).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (1).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (2).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (3).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (4).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (5).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (6).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (7).jpg  
  inflating: PlantDoc-Dataset/test/Potato leaf late blight/Potato leaf late blight (8).jpg  
  inflating: PlantDoc-Dataset/test/Raspberry leaf/Raspberry leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Raspberry leaf/Raspberry leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Raspberry leaf/Raspberry leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Raspberry leaf/Raspberry leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Raspberry leaf/Raspberry leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Raspberry leaf/Raspberry leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Raspberry leaf/Raspberry leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Soyabean leaf/Soyabean leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Squash Powdery mildew leaf/Squash Powdery mildew leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Squash Powdery mildew leaf/Squash Powdery mildew leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Squash Powdery mildew leaf/Squash Powdery mildew leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Squash Powdery mildew leaf/Squash Powdery mildew leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Squash Powdery mildew leaf/Squash Powdery mildew leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Squash Powdery mildew leaf/Squash Powdery mildew leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Strawberry leaf/Strawberry leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Early blight leaf/Tomato Early blight leaf (9).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (10).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (11).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (6).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (7).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (8).jpg  
  inflating: PlantDoc-Dataset/test/Tomato Septoria leaf spot/Tomato Septoria leaf spot (9).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (6).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (7).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (8).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf bacterial spot/Tomato leaf bacterial spot (9).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (10).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (6).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (7).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (8).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf late blight/Tomato leaf late blight (9).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (10).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (6).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (7).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (8).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf mosaic virus/Tomato leaf mosaic virus (9).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf yellow virus/Tomato leaf yellow virus (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf yellow virus/Tomato leaf yellow virus (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf yellow virus/Tomato leaf yellow virus (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf yellow virus/Tomato leaf yellow virus (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf yellow virus/Tomato leaf yellow virus (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf yellow virus/Tomato leaf yellow virus (6).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/Tomato leaf/Tomato leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/Tomato mold leaf/Tomato mold leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/Tomato mold leaf/Tomato mold leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/Tomato mold leaf/Tomato mold leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/Tomato mold leaf/Tomato mold leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/Tomato mold leaf/Tomato mold leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/Tomato mold leaf/Tomato mold leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (1).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (2).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (3).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (4).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (5).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (6).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (7).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf black rot/grape leaf black rot (8).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (1).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (10).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (11).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (12).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (2).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (3).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (4).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (5).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (6).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (7).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (8).jpg  
  inflating: PlantDoc-Dataset/test/grape leaf/grape leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Apple Scab Leaf/Apple Scab Leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Apple leaf/Apple leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Apple rust leaf/Apple rust leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (1).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (10).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (11).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (12).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (13).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (14).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (15).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (16).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (17).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (18).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (19).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (2).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (20).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (21).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (22).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (23).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (24).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (25).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (26).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (27).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (28).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (29).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (3).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (30).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (31).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (32).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (33).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (34).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (35).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (36).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (37).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (38).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (39).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (4).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (40).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (41).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (42).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (43).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (44).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (45).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (46).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (47).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (48).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (49).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (5).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (50).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (51).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (52).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (53).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (54).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (55).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (56).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (57).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (58).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (59).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (6).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (60).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (61).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (62).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (7).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (8).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf spot/Bell_pepper leaf spot (9).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Bell_pepper leaf/Bell_pepper leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (100).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (101).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (102).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (103).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (104).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (105).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (83).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (84).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (85).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (86).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (87).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (88).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (89).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (90).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (91).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (92).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (93).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (94).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (95).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (96).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (97).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (98).jpg  
  inflating: PlantDoc-Dataset/train/Blueberry leaf/Blueberry leaf (99).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Cherry leaf/Cherry leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (1).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (10).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (11).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (12).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (13).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (14).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (15).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (16).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (17).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (18).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (19).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (2).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (20).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (21).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (22).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (23).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (24).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (25).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (26).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (27).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (28).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (29).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (3).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (30).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (31).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (32).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (33).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (34).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (35).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (36).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (37).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (38).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (39).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (4).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (40).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (41).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (42).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (43).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (44).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (45).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (46).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (47).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (48).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (49).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (5).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (50).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (51).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (52).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (53).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (54).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (55).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (56).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (57).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (58).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (59).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (6).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (60).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (61).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (62).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (63).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (64).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (7).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (8).jpg  
  inflating: PlantDoc-Dataset/train/Corn Gray leaf spot/Corn Gray leaf spot (9).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (1).jpeg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (1).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (10).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (100).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (101).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (102).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (103).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (104).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (105).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (106).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (107).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (108).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (109).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (11).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (110).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (111).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (112).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (113).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (114).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (115).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (116).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (117).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (118).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (119).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (12).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (120).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (121).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (122).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (123).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (124).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (125).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (126).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (127).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (128).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (129).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (13).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (130).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (131).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (132).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (133).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (134).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (135).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (136).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (137).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (138).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (139).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (14).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (140).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (141).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (142).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (143).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (144).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (145).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (146).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (147).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (148).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (149).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (15).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (150).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (151).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (152).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (153).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (154).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (155).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (156).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (157).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (158).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (159).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (16).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (160).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (161).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (162).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (163).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (164).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (165).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (166).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (167).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (168).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (169).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (17).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (170).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (171).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (172).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (173).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (174).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (175).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (176).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (177).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (178).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (179).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (18).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (19).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (2).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (20).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (21).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (22).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (23).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (24).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (25).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (26).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (27).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (28).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (29).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (3).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (30).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (31).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (32).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (33).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (34).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (35).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (36).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (37).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (38).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (39).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (4).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (40).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (41).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (42).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (43).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (44).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (45).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (46).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (47).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (48).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (49).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (5).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (50).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (51).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (52).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (53).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (54).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (55).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (56).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (57).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (58).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (59).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (6).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (60).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (61).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (62).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (63).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (64).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (65).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (66).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (67).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (68).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (69).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (7).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (70).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (71).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (72).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (73).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (74).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (75).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (76).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (77).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (78).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (79).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (8).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (80).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (81).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (82).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (83).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (84).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (85).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (86).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (87).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (88).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (89).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (9).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (90).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (91).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (92).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (93).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (94).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (95).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (96).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (97).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (98).jpg  
  inflating: PlantDoc-Dataset/train/Corn leaf blight/Corn leaf blight (99).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (100).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (101).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (102).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (103).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (104).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (105).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (106).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (83).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (84).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (85).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (86).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (87).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (88).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (89).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (90).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (91).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (92).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (93).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (94).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (95).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (96).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (97).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (98).jpg  
  inflating: PlantDoc-Dataset/train/Corn rust leaf/Corn rust leaf (99).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (100).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (101).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (102).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (103).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (83).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (84).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (85).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (86).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (87).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (88).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (89).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (90).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (91).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (92).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (93).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (94).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (95).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (96).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (97).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (98).jpg  
  inflating: PlantDoc-Dataset/train/Peach leaf/Peach leaf (99).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (1).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (10).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (100).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (101).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (102).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (103).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (104).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (105).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (106).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (107).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (108).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (109).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (11).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (12).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (13).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (14).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (15).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (16).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (17).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (18).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (19).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (2).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (20).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (21).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (22).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (23).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (24).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (25).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (26).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (27).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (28).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (29).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (3).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (30).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (31).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (32).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (33).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (34).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (35).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (36).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (37).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (38).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (39).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (4).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (40).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (41).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (42).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (43).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (44).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (45).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (46).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (47).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (48).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (49).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (5).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (50).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (51).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (52).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (53).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (54).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (55).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (56).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (57).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (58).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (59).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (6).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (60).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (61).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (62).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (63).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (64).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (65).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (66).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (67).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (68).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (69).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (7).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (70).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (71).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (72).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (73).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (74).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (75).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (76).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (77).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (78).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (79).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (8).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (80).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (81).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (82).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (83).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (84).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (85).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (86).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (87).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (88).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (89).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (9).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (90).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (91).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (92).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (93).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (94).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (95).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (96).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (97).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (98).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf early blight/Potato leaf early blight (99).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (1).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (10).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (11).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (12).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (13).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (14).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (15).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (16).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (17).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (18).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (19).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (2).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (20).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (21).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (22).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (23).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (24).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (25).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (26).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (27).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (28).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (29).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (3).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (30).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (31).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (32).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (33).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (34).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (35).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (36).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (37).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (38).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (39).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (4).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (40).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (41).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (42).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (43).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (44).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (45).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (46).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (47).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (48).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (49).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (5).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (50).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (51).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (52).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (53).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (54).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (55).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (56).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (57).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (58).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (59).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (6).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (60).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (61).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (62).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (63).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (64).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (65).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (66).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (67).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (68).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (69).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (7).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (70).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (71).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (72).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (73).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (74).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (75).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (76).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (77).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (78).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (79).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (8).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (80).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (81).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (82).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (83).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (84).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (85).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (86).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (87).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (88).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (89).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (9).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (90).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (91).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (92).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (93).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (94).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (95).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (96).jpg  
  inflating: PlantDoc-Dataset/train/Potato leaf late blight/Potato leaf late blight (97).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (100).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (101).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (102).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (103).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (104).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (105).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (106).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (107).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (108).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (109).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (83).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (84).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (85).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (86).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (87).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (88).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (89).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (90).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (91).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (92).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (93).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (94).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (95).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (96).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (97).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (98).jpg  
  inflating: PlantDoc-Dataset/train/Raspberry leaf/Raspberry leaf (99).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Soyabean leaf/Soyabean leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (100).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (101).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (102).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (103).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (104).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (105).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (106).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (107).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (108).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (109).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (110).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (111).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (112).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (113).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (114).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (115).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (116).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (117).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (118).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (119).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (120).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (121).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (122).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (123).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (83).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (84).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (85).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (86).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (87).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (88).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (89).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (90).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (91).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (92).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (93).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (94).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (95).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (96).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (97).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (98).jpg  
  inflating: PlantDoc-Dataset/train/Squash Powdery mildew leaf/Squash Powdery mildew leaf (99).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (83).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (84).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (85).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (86).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (87).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (88).jpg  
  inflating: PlantDoc-Dataset/train/Strawberry leaf/Strawberry leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Early blight leaf/Tomato Early blight leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (1).png  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (100).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (101).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (102).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (103).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (104).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (105).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (106).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (107).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (108).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (109).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (110).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (111).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (112).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (113).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (114).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (115).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (116).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (117).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (118).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (119).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (120).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (121).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (122).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (123).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (124).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (125).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (126).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (127).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (128).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (129).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (130).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (131).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (132).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (133).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (134).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (135).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (136).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (45).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (46).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (47).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (48).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (49).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (50).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (51).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (52).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (53).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (54).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (55).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (56).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (57).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (58).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (59).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (60).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (61).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (62).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (63).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (64).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (65).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (66).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (67).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (68).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (69).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (70).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (71).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (72).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (73).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (74).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (75).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (76).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (77).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (78).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (79).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (80).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (81).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (82).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (83).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (84).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (85).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (86).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (87).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (88).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (89).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (90).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (91).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (92).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (93).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (94).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (95).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (96).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (97).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (98).jpg  
  inflating: PlantDoc-Dataset/train/Tomato Septoria leaf spot/Tomato Septoria leaf spot (99).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (45).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (46).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (47).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (48).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (49).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (50).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (51).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (52).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (53).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (54).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (55).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (56).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (57).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (58).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (59).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (60).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (61).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (62).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (63).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (64).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (65).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (66).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (67).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (68).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (69).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (70).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (71).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (72).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (73).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (74).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (75).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (76).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (77).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (78).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (79).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (80).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (81).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (82).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (83).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (84).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (85).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (86).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (87).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (88).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (89).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (90).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (91).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (92).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (93).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (94).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (95).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (96).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (97).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf bacterial spot/Tomato leaf bacterial spot (98).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (100).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (101).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (45).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (46).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (47).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (48).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (49).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (50).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (51).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (52).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (53).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (54).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (55).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (56).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (57).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (58).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (59).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (60).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (61).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (62).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (63).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (64).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (65).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (66).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (67).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (68).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (69).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (70).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (71).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (72).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (73).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (74).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (75).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (76).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (77).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (78).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (79).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (80).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (81).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (82).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (83).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (84).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (85).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (86).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (87).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (88).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (89).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (90).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (91).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (92).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (93).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (94).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (95).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (96).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (97).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (98).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf late blight/Tomato leaf late blight (99).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf mosaic virus/Tomato leaf mosaic virus (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (45).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (46).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (47).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (48).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (49).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (50).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (51).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (52).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (53).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (54).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (55).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (56).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (57).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (58).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (59).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (60).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (61).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (62).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (63).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (64).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (65).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (66).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (67).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (68).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (69).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf yellow virus/Tomato leaf yellow virus (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato leaf/Tomato leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (58).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (59).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (60).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (61).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (62).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (63).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (64).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (65).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (66).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (67).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (68).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (69).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (70).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (71).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (72).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (73).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (74).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (75).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (76).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (77).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (78).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (79).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (80).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (81).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (82).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (83).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (84).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (85).jpg  
  inflating: PlantDoc-Dataset/train/Tomato mold leaf/Tomato mold leaf (9).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (1).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (10).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (11).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (12).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (13).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (14).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (15).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (16).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (17).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (18).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (19).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (2).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (20).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (21).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (22).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (23).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (24).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (25).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (26).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (27).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (28).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (29).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (3).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (30).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (31).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (32).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (33).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (34).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (35).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (36).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (37).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (38).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (39).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (4).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (40).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (41).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (42).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (43).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (44).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (45).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (46).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (47).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (48).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (49).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (5).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (50).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (51).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (52).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (53).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (54).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (55).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (56).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (6).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (7).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (8).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf black rot/grape leaf black rot (9).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (1).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (10).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (11).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (12).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (13).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (14).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (15).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (16).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (17).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (18).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (19).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (2).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (20).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (21).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (22).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (23).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (24).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (25).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (26).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (27).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (28).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (29).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (3).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (30).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (31).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (32).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (33).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (34).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (35).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (36).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (37).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (38).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (39).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (4).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (40).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (41).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (42).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (43).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (44).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (45).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (46).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (47).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (48).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (49).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (5).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (50).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (51).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (52).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (53).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (54).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (55).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (56).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (57).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (6).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (7).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (8).jpg  
  inflating: PlantDoc-Dataset/train/grape leaf/grape leaf (9).jpg  
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell" id="cell-fW7FM7sl9K9_" role="region" aria-label="Cell 4: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;os</span></span><br><span><span></span></span><br><span><span class="mtk20">for</span><span class="mtk1">&nbsp;root</span><span class="mtk14">,</span><span class="mtk1">&nbsp;dirs</span><span class="mtk14">,</span><span class="mtk1">&nbsp;files&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;os.walk</span><span class="mtk14">(</span><span class="mtk5">"data"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;topdown=</span><span class="mtk9">True</span><span class="mtk14">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk1">root</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk17">len</span><span class="mtk14">(</span><span class="mtk1">files</span><span class="mtk14">))</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 4 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell" id="cell-ccoccpSR-Exb" role="region" aria-label="Cell 5: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk1">base_dir&nbsp;=&nbsp;</span><span class="mtk5">"/content/PlantDoc-Dataset/train"</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 5 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-zjnN93AmowMx" role="region" aria-label="Cell 6: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;os</span></span><br><span><span></span></span><br><span><span class="mtk1">classes&nbsp;=&nbsp;os.listdir</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">plants&nbsp;=&nbsp;</span><span class="mtk16">set</span><span class="mtk14">()</span></span><br><span><span></span></span><br><span><span class="mtk20">for</span><span class="mtk1">&nbsp;c&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;classes</span><span class="mtk14">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plant&nbsp;=&nbsp;c.split</span><span class="mtk14">(</span><span class="mtk5">"&nbsp;"</span><span class="mtk14">)[</span><span class="mtk6">0</span><span class="mtk14">]</span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;plant&nbsp;name</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plants.add</span><span class="mtk14">(</span><span class="mtk1">plant</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk5">"Plants&nbsp;present&nbsp;in&nbsp;dataset:"</span><span class="mtk14">)</span></span><br><span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk1">plants</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 6 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Plants present in dataset:
{'Potato', 'Corn', 'Cherry', 'Squash', 'Blueberry', 'Strawberry', 'Bell_pepper', 'Peach', 'Tomato', 'Raspberry', 'grape', 'Apple', 'Soyabean'}
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-TBX7THPMox26" role="region" aria-label="Cell 7: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk1">plant_dict&nbsp;=&nbsp;</span><span class="mtk14">{}</span></span><br><span><span></span></span><br><span><span class="mtk20">for</span><span class="mtk1">&nbsp;c&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;classes</span><span class="mtk14">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plant&nbsp;=&nbsp;c.split</span><span class="mtk14">(</span><span class="mtk5">"_"</span><span class="mtk14">)[</span><span class="mtk6">0</span><span class="mtk14">]</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;plant&nbsp;</span><span class="mtk19">not</span><span class="mtk1">&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;plant_dict</span><span class="mtk14">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;plant_dict</span><span class="mtk14">[</span><span class="mtk1">plant</span><span class="mtk14">]</span><span class="mtk1">&nbsp;=&nbsp;</span><span class="mtk14">[]</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plant_dict</span><span class="mtk14">[</span><span class="mtk1">plant</span><span class="mtk14">]</span><span class="mtk1">.append</span><span class="mtk14">(</span><span class="mtk1">c</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk20">for</span><span class="mtk1">&nbsp;plant&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;plant_dict</span><span class="mtk14">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk5">"\nPlant:"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;plant</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">for</span><span class="mtk1">&nbsp;disease&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;plant_dict</span><span class="mtk14">[</span><span class="mtk1">plant</span><span class="mtk14">]:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk5">"&nbsp;&nbsp;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;disease</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 7 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>
Plant: Tomato Early blight leaf
   Tomato Early blight leaf

Plant: grape leaf
   grape leaf

Plant: Tomato Septoria leaf spot
   Tomato Septoria leaf spot

Plant: Corn Gray leaf spot
   Corn Gray leaf spot

Plant: Tomato mold leaf
   Tomato mold leaf

Plant: Corn leaf blight
   Corn leaf blight

Plant: Apple rust leaf
   Apple rust leaf

Plant: Strawberry leaf
   Strawberry leaf

Plant: Tomato leaf yellow virus
   Tomato leaf yellow virus

Plant: Cherry leaf
   Cherry leaf

Plant: Blueberry leaf
   Blueberry leaf

Plant: Raspberry leaf
   Raspberry leaf

Plant: Tomato leaf mosaic virus
   Tomato leaf mosaic virus

Plant: Apple Scab Leaf
   Apple Scab Leaf

Plant: Tomato leaf
   Tomato leaf

Plant: Corn rust leaf
   Corn rust leaf

Plant: Tomato leaf bacterial spot
   Tomato leaf bacterial spot

Plant: Bell
   Bell_pepper leaf spot
   Bell_pepper leaf

Plant: Apple leaf
   Apple leaf

Plant: Potato leaf late blight
   Potato leaf late blight

Plant: grape leaf black rot
   grape leaf black rot

Plant: Potato leaf early blight
   Potato leaf early blight

Plant: Tomato leaf late blight
   Tomato leaf late blight

Plant: Squash Powdery mildew leaf
   Squash Powdery mildew leaf

Plant: Peach leaf
   Peach leaf

Plant: Soyabean leaf
   Soyabean leaf
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-0QVqYR-4DzZ-" role="region" aria-label="Cell 8: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk1">os.listdir</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">))</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 8 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>['Tomato Early blight leaf', 'grape leaf', 'Tomato Septoria leaf spot', 'Corn Gray leaf spot', 'Tomato mold leaf', 'Corn leaf blight', 'Apple rust leaf', 'Strawberry leaf', 'Tomato leaf yellow virus', 'Cherry leaf', 'Blueberry leaf', 'Raspberry leaf', 'Tomato leaf mosaic virus', 'Apple Scab Leaf', 'Tomato leaf', 'Corn rust leaf', 'Tomato leaf bacterial spot', 'Bell_pepper leaf spot', 'Apple leaf', 'Potato leaf late blight', 'grape leaf black rot', 'Potato leaf early blight', 'Bell_pepper leaf', 'Tomato leaf late blight', 'Squash Powdery mildew leaf', 'Peach leaf', 'Soyabean leaf']
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-az5d47USC2Ch" role="region" aria-label="Cell 9: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;os</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;random</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;cv2</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;plt</span></span><br><span><span></span></span><br><span><span class="mtk1">plant_name&nbsp;=&nbsp;</span><span class="mtk5">"Corn"</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;find&nbsp;classes&nbsp;containing&nbsp;that&nbsp;plant</span></span><br><span><span class="mtk1">plant_classes&nbsp;=&nbsp;</span><span class="mtk14">[</span><span class="mtk1">c&nbsp;</span><span class="mtk20">for</span><span class="mtk1">&nbsp;c&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;os.listdir</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">)</span><span class="mtk1">&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;plant_name.lower</span><span class="mtk14">()</span><span class="mtk1">&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;c.lower</span><span class="mtk14">()]</span></span><br><span><span></span></span><br><span><span class="mtk1">plt.figure</span><span class="mtk14">(</span><span class="mtk1">figsize=</span><span class="mtk14">(</span><span class="mtk6">12</span><span class="mtk14">,</span><span class="mtk6">12</span><span class="mtk14">))</span></span><br><span><span></span></span><br><span><span class="mtk20">for</span><span class="mtk1">&nbsp;i&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;</span><span class="mtk17">range</span><span class="mtk14">(</span><span class="mtk6">2</span><span class="mtk14">):</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sample_class&nbsp;=&nbsp;random.choice</span><span class="mtk14">(</span><span class="mtk1">plant_classes</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sample_image&nbsp;=&nbsp;random.choice</span><span class="mtk14">(</span><span class="mtk1">os.listdir</span><span class="mtk14">(</span><span class="mtk1">os.path.join</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">,</span><span class="mtk1">&nbsp;sample_class</span><span class="mtk14">)))</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img_path&nbsp;=&nbsp;os.path.join</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">,</span><span class="mtk1">&nbsp;sample_class</span><span class="mtk14">,</span><span class="mtk1">&nbsp;sample_image</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;cv2.imread</span><span class="mtk14">(</span><span class="mtk1">img_path</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;cv2.cvtColor</span><span class="mtk14">(</span><span class="mtk1">img</span><span class="mtk14">,</span><span class="mtk1">&nbsp;cv2.COLOR_BGR2RGB</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.subplot</span><span class="mtk14">(</span><span class="mtk6">3</span><span class="mtk14">,</span><span class="mtk6">3</span><span class="mtk14">,</span><span class="mtk1">i+</span><span class="mtk6">1</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.imshow</span><span class="mtk14">(</span><span class="mtk1">img</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.title</span><span class="mtk14">(</span><span class="mtk1">sample_class</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.axis</span><span class="mtk14">(</span><span class="mtk5">"off"</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">plt.show</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 9 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 278px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./MajorProject (3)_files/outputframe(1).html" class="" style="height: 278px;" tabindex="-1"></iframe></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-DilsFP74DXju" role="region" aria-label="Cell 10: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;os</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;cv2</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;plt</span></span><br><span><span></span></span><br><span><span class="mtk1">class_name&nbsp;=&nbsp;</span><span class="mtk5">"Potato&nbsp;leaf&nbsp;early&nbsp;blight"</span></span><br><span><span></span></span><br><span><span class="mtk1">folder_path&nbsp;=&nbsp;os.path.join</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">,</span><span class="mtk1">&nbsp;class_name</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">images&nbsp;=&nbsp;os.listdir</span><span class="mtk14">(</span><span class="mtk1">folder_path</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">plt.figure</span><span class="mtk14">(</span><span class="mtk1">figsize=</span><span class="mtk14">(</span><span class="mtk6">10</span><span class="mtk14">,</span><span class="mtk6">10</span><span class="mtk14">))</span></span><br><span><span></span></span><br><span><span class="mtk20">for</span><span class="mtk1">&nbsp;i&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;</span><span class="mtk17">range</span><span class="mtk14">(</span><span class="mtk6">9</span><span class="mtk14">):</span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;show&nbsp;9&nbsp;images</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img_path&nbsp;=&nbsp;os.path.join</span><span class="mtk14">(</span><span class="mtk1">folder_path</span><span class="mtk14">,</span><span class="mtk1">&nbsp;images</span><span class="mtk14">[</span><span class="mtk1">i</span><span class="mtk14">])</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;cv2.imread</span><span class="mtk14">(</span><span class="mtk1">img_path</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;cv2.cvtColor</span><span class="mtk14">(</span><span class="mtk1">img</span><span class="mtk14">,</span><span class="mtk1">&nbsp;cv2.COLOR_BGR2RGB</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.subplot</span><span class="mtk14">(</span><span class="mtk6">3</span><span class="mtk14">,</span><span class="mtk6">3</span><span class="mtk14">,</span><span class="mtk1">i+</span><span class="mtk6">1</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.imshow</span><span class="mtk14">(</span><span class="mtk1">img</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.title</span><span class="mtk14">(</span><span class="mtk1">class_name</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.axis</span><span class="mtk14">(</span><span class="mtk5">"off"</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">plt.show</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 10 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 776px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./MajorProject (3)_files/outputframe(2).html" class="" style="height: 776px;" tabindex="-1"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-_kpBnJuT98S1" role="region" aria-label="Cell 11: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;plt</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;random</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;os</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;cv2</span></span><br><span><span></span></span><br><span><span class="mtk1">plt.figure</span><span class="mtk14">(</span><span class="mtk1">figsize=</span><span class="mtk14">(</span><span class="mtk6">12</span><span class="mtk14">,</span><span class="mtk6">12</span><span class="mtk14">))</span></span><br><span><span></span></span><br><span><span class="mtk1">num_images&nbsp;=&nbsp;</span><span class="mtk6">25</span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;number&nbsp;of&nbsp;images&nbsp;you&nbsp;want</span></span><br><span><span></span></span><br><span><span class="mtk20">for</span><span class="mtk1">&nbsp;i&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;</span><span class="mtk17">range</span><span class="mtk14">(</span><span class="mtk1">num_images</span><span class="mtk14">):</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sample_class&nbsp;=&nbsp;random.choice</span><span class="mtk14">(</span><span class="mtk1">os.listdir</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">))</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sample_image&nbsp;=&nbsp;random.choice</span><span class="mtk14">(</span><span class="mtk1">os.listdir</span><span class="mtk14">(</span><span class="mtk1">os.path.join</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">,</span><span class="mtk1">&nbsp;sample_class</span><span class="mtk14">)))</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img_path&nbsp;=&nbsp;os.path.join</span><span class="mtk14">(</span><span class="mtk1">base_dir</span><span class="mtk14">,</span><span class="mtk1">&nbsp;sample_class</span><span class="mtk14">,</span><span class="mtk1">&nbsp;sample_image</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;cv2.imread</span><span class="mtk14">(</span><span class="mtk1">img_path</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;cv2.cvtColor</span><span class="mtk14">(</span><span class="mtk1">img</span><span class="mtk14">,</span><span class="mtk1">&nbsp;cv2.COLOR_BGR2RGB</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.subplot</span><span class="mtk14">(</span><span class="mtk6">5</span><span class="mtk14">,</span><span class="mtk6">5</span><span class="mtk14">,</span><span class="mtk1">i+</span><span class="mtk6">1</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.imshow</span><span class="mtk14">(</span><span class="mtk1">img</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.title</span><span class="mtk14">(</span><span class="mtk1">sample_class</span><span class="mtk14">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.axis</span><span class="mtk14">(</span><span class="mtk5">"off"</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">plt.show</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 11 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 983px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./MajorProject (3)_files/outputframe(3).html" class="" style="height: 983px;" tabindex="-1"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-j43Fo99-_Iya" role="region" aria-label="Cell 12: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;IMAGE&nbsp;PREPROCESSING</span></span><br><span><span></span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;tensorflow&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;tf</span></span><br><span><span class="mtk20">from</span><span class="mtk1">&nbsp;tensorflow.keras.preprocessing.image&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;ImageDataGenerator</span></span><br><span><span></span></span><br><span><span class="mtk1">IMG_SIZE&nbsp;=&nbsp;</span><span class="mtk6">64</span></span><br><span><span class="mtk1">BATCH_SIZE&nbsp;=&nbsp;</span><span class="mtk6">32</span></span><br><span><span></span></span><br><span><span class="mtk1">train_datagen&nbsp;=&nbsp;ImageDataGenerator</span><span class="mtk14">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;rescale=</span><span class="mtk6">1</span><span class="mtk1">./</span><span class="mtk6">255</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;validation_split=</span><span class="mtk6">0.2</span></span><br><span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">train_data&nbsp;=&nbsp;train_datagen.flow_from_directory</span><span class="mtk14">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;base_dir</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;target_size=</span><span class="mtk14">(</span><span class="mtk1">IMG_SIZE</span><span class="mtk14">,</span><span class="mtk1">&nbsp;IMG_SIZE</span><span class="mtk14">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;batch_size=BATCH_SIZE</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;class_mode=</span><span class="mtk5">'categorical'</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;subset=</span><span class="mtk5">'training'</span></span><br><span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">val_data&nbsp;=&nbsp;train_datagen.flow_from_directory</span><span class="mtk14">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;base_dir</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;target_size=</span><span class="mtk14">(</span><span class="mtk1">IMG_SIZE</span><span class="mtk14">,</span><span class="mtk1">&nbsp;IMG_SIZE</span><span class="mtk14">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;batch_size=BATCH_SIZE</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;class_mode=</span><span class="mtk5">'categorical'</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;subset=</span><span class="mtk5">'validation'</span></span><br><span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 12 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Found 1866 images belonging to 27 classes.
Found 450 images belonging to 27 classes.
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-_u8CPIas_K0h" role="region" aria-label="Cell 13: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;np</span></span><br><span><span></span></span><br><span><span class="mtk1">X_batch</span><span class="mtk14">,</span><span class="mtk1">&nbsp;y_batch&nbsp;=&nbsp;</span><span class="mtk17">next</span><span class="mtk14">(</span><span class="mtk1">train_data</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;flatten&nbsp;images</span></span><br><span><span class="mtk1">features&nbsp;=&nbsp;X_batch.reshape</span><span class="mtk14">(</span><span class="mtk1">X_batch.shape</span><span class="mtk14">[</span><span class="mtk6">0</span><span class="mtk14">],</span><span class="mtk1">&nbsp;</span><span class="mtk6">-1</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;reduce&nbsp;features&nbsp;for&nbsp;quantum&nbsp;circuit</span></span><br><span><span class="mtk1">features&nbsp;=&nbsp;features</span><span class="mtk14">[:,</span><span class="mtk1">&nbsp;</span><span class="mtk14">:</span><span class="mtk6">4</span><span class="mtk14">]</span></span><br><span><span></span></span><br><span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk1">features.shape</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 13 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>(32, 4)
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-SYGfxx-__PKc" role="region" aria-label="Cell 14: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk19">!</span><span class="mtk1">pip&nbsp;install&nbsp;qiskit&nbsp;qiskit-machine-learning</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 14 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Collecting qiskit
  Downloading qiskit-2.3.0-cp310-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (12 kB)
Collecting qiskit-machine-learning
  Downloading qiskit_machine_learning-0.9.0-py3-none-any.whl.metadata (13 kB)
Collecting rustworkx&gt;=0.15.0 (from qiskit)
  Downloading rustworkx-0.17.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (10 kB)
Requirement already satisfied: numpy&lt;3,&gt;=1.17 in /usr/local/lib/python3.12/dist-packages (from qiskit) (2.0.2)
Requirement already satisfied: scipy&gt;=1.5 in /usr/local/lib/python3.12/dist-packages (from qiskit) (1.16.3)
Requirement already satisfied: dill&gt;=0.3 in /usr/local/lib/python3.12/dist-packages (from qiskit) (0.3.8)
Collecting stevedore&gt;=3.0.0 (from qiskit)
  Downloading stevedore-5.7.0-py3-none-any.whl.metadata (2.4 kB)
Requirement already satisfied: typing-extensions in /usr/local/lib/python3.12/dist-packages (from qiskit) (4.15.0)
Requirement already satisfied: scikit-learn&gt;=1.2 in /usr/local/lib/python3.12/dist-packages (from qiskit-machine-learning) (1.6.1)
Requirement already satisfied: setuptools&gt;=40.1 in /usr/local/lib/python3.12/dist-packages (from qiskit-machine-learning) (75.2.0)
Requirement already satisfied: joblib&gt;=1.2.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn&gt;=1.2-&gt;qiskit-machine-learning) (1.5.3)
Requirement already satisfied: threadpoolctl&gt;=3.1.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn&gt;=1.2-&gt;qiskit-machine-learning) (3.6.0)
Downloading qiskit-2.3.0-cp310-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (8.9 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">8.9/8.9 MB</span><span> </span><span style="color: var(--ansi-red);">35.0 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading qiskit_machine_learning-0.9.0-py3-none-any.whl (263 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">263.1/263.1 kB</span><span> </span><span style="color: var(--ansi-red);">17.3 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading rustworkx-0.17.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.2 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">2.2/2.2 MB</span><span> </span><span style="color: var(--ansi-red);">56.5 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading stevedore-5.7.0-py3-none-any.whl (54 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">54.5/54.5 kB</span><span> </span><span style="color: var(--ansi-red);">3.5 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Installing collected packages: stevedore, rustworkx, qiskit, qiskit-machine-learning
Successfully installed qiskit-2.3.0 qiskit-machine-learning-0.9.0 rustworkx-0.17.1 stevedore-5.7.0
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-ri6RrcJj_QVp" role="region" aria-label="Cell 15: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk19">!</span><span class="mtk1">pip&nbsp;install&nbsp;pylatexenc</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 15 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Requirement already satisfied: pylatexenc in /usr/local/lib/python3.12/dist-packages (2.10)
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell" id="cell-1tGhkzn1FZbs" role="region" aria-label="Cell 16: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;os</span></span><br><span><span class="mtk1">os.kill</span><span class="mtk14">(</span><span class="mtk1">os.getpid</span><span class="mtk14">(),</span><span class="mtk1">&nbsp;</span><span class="mtk6">9</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 16 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-ROC-t5-jFdcf" role="region" aria-label="Cell 17: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;qiskit.circuit.library&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;ZZFeatureMap</span></span><br><span><span></span></span><br><span><span class="mtk1">feature_map&nbsp;=&nbsp;ZZFeatureMap</span><span class="mtk14">(</span><span class="mtk1">feature_dimension=</span><span class="mtk6">4</span><span class="mtk14">,</span><span class="mtk1">&nbsp;reps=</span><span class="mtk6">2</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">feature_map.draw</span><span class="mtk14">(</span><span class="mtk5">'mpl'</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 17 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 375px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./MajorProject (3)_files/outputframe(4).html" class="" style="height: 375px;" tabindex="-1"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-mr0u4TAQFqhe" role="region" aria-label="Cell 18: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;qiskit.circuit.library&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;TwoLocal</span></span><br><span><span></span></span><br><span><span class="mtk1">ansatz&nbsp;=&nbsp;TwoLocal</span><span class="mtk14">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;num_qubits=</span><span class="mtk6">4</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;rotation_blocks=</span><span class="mtk5">'ry'</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;entanglement_blocks=</span><span class="mtk5">'cz'</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;reps=</span><span class="mtk6">2</span></span><br><span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">ansatz.draw</span><span class="mtk14">(</span><span class="mtk5">'mpl'</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 18 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 375px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./MajorProject (3)_files/outputframe(5).html" class="" style="height: 375px;" tabindex="-1"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-BEQCDm1JGGhP" role="region" aria-label="Cell 19: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk19">!</span><span class="mtk1">pip&nbsp;install&nbsp;qiskit-algorithms</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 19 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Collecting qiskit-algorithms
  Downloading qiskit_algorithms-0.4.0-py3-none-any.whl.metadata (4.7 kB)
Requirement already satisfied: qiskit&gt;=1.0 in /usr/local/lib/python3.12/dist-packages (from qiskit-algorithms) (2.3.0)
Requirement already satisfied: scipy&gt;=1.4 in /usr/local/lib/python3.12/dist-packages (from qiskit-algorithms) (1.16.3)
Requirement already satisfied: numpy&gt;=1.17 in /usr/local/lib/python3.12/dist-packages (from qiskit-algorithms) (2.0.2)
Requirement already satisfied: rustworkx&gt;=0.15.0 in /usr/local/lib/python3.12/dist-packages (from qiskit&gt;=1.0-&gt;qiskit-algorithms) (0.17.1)
Requirement already satisfied: dill&gt;=0.3 in /usr/local/lib/python3.12/dist-packages (from qiskit&gt;=1.0-&gt;qiskit-algorithms) (0.3.8)
Requirement already satisfied: stevedore&gt;=3.0.0 in /usr/local/lib/python3.12/dist-packages (from qiskit&gt;=1.0-&gt;qiskit-algorithms) (5.7.0)
Requirement already satisfied: typing-extensions in /usr/local/lib/python3.12/dist-packages (from qiskit&gt;=1.0-&gt;qiskit-algorithms) (4.15.0)
Downloading qiskit_algorithms-0.4.0-py3-none-any.whl (327 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">327.8/327.8 kB</span><span> </span><span style="color: var(--ansi-red);">5.7 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Installing collected packages: qiskit-algorithms
Successfully installed qiskit-algorithms-0.4.0
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell" id="cell-SfAPvvyuGNU_" role="region" aria-label="Cell 20: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;os</span></span><br><span><span class="mtk1">os.kill</span><span class="mtk14">(</span><span class="mtk1">os.getpid</span><span class="mtk14">(),</span><span class="mtk6">9</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 20 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-JZpOS1nvGIew" role="region" aria-label="Cell 21: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;qiskit_machine_learning.algorithms&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;VQC</span></span><br><span><span class="mtk20">from</span><span class="mtk1">&nbsp;qiskit_algorithms.optimizers&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;COBYLA</span></span><br><span><span></span></span><br><span><span class="mtk1">vqc&nbsp;=&nbsp;VQC</span><span class="mtk14">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;feature_map=feature_map</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;ansatz=ansatz</span><span class="mtk14">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;optimizer=COBYLA</span><span class="mtk14">(</span><span class="mtk1">maxiter=</span><span class="mtk6">100</span><span class="mtk14">)</span></span><br><span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 21 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>WARNING:qiskit_machine_learning.neural_networks.sampler_qnn:No gradient function provided, creating a gradient function. If your Sampler requires transpilation, please provide a pass manager.
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell focused" id="cell-_b6FaVv7HrHs" role="region" aria-label="Cell 22: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->arrow_upward</md-icon>
        <!--?lit$091463802$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Move cell up</div><!----><!----><div><!--?lit$091463802$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->arrow_downward</md-icon>
        <!--?lit$091463802$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Move cell down</div><!----><!----><div><!--?lit$091463802$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$091463802$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-_b6FaVv7HrHs" anchor="ai-menu-anchor-_b6FaVv7HrHs" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$091463802$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$091463802$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$091463802$--><!----><md-menu-item command="generate-code" md-menu-item=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   "><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   "><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   "><!--?lit$091463802$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$091463802$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$091463802$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$091463802$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$091463802$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-_b6FaVv7HrHs-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-_b6FaVv7HrHs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template> pen_spark </md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-_b6FaVv7HrHs" id="ai-menu-anchor-_b6FaVv7HrHs-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->edit</md-icon>
        <!--?lit$091463802$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->delete</md-icon>
        <!--?lit$091463802$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Delete cell</div><!----><!----><div><!--?lit$091463802$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Marthala Bhargavi
1:20 PM (5 hours ago)
executed in 0.015s"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed by Marthala Bhargavi</div><!----><!----><div><!--?lit$091463802$-->1:20 PM (5 hours ago)</div><!----><!----><div><!--?lit$091463802$-->executed in 0.015s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="157" data-mode-id="notebook-python" style="height: 86px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/25" style="width: 1722px; height: 86px;"><div data-mprt="3" class="overflow-guard" style="width: 1722px; height: 86px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 86px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 86px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 86px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1716px; height: 86px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 86px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1716px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1716px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1716px; height: 86px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;np</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">features&nbsp;=&nbsp;np.random.rand</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk6">50</span><span class="mtk14">,</span><span class="mtk6">4</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;50&nbsp;samples,&nbsp;4&nbsp;features</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">y_batch&nbsp;=&nbsp;np.random.randint</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk6">0</span><span class="mtk14">,</span><span class="mtk6">2</span><span class="mtk14">,</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk6">50</span><span class="mtk14">,</span><span class="mtk6">2</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1702px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1702px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="86" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 86px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 86px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 86px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1722px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="-1" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1722px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 86px;"><div class="minimap-shadow-hidden" style="height: 86px;"></div><canvas width="0" height="86" style="position: absolute; left: 0px; width: 0px; height: 86px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="86" style="position: absolute; left: 0px; width: 0px; height: 86px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1920px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 1136.52px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 22 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button focused" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer role="group"><div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-az3SAOexHtBe" role="region" aria-label="Cell 23: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk1">X_train&nbsp;=&nbsp;features</span></span><br><span><span class="mtk1">y_train&nbsp;=&nbsp;np.argmax</span><span class="mtk14">(</span><span class="mtk1">y_batch</span><span class="mtk14">,</span><span class="mtk1">&nbsp;axis=</span><span class="mtk6">1</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk1">vqc.fit</span><span class="mtk14">(</span><span class="mtk1">X_train</span><span class="mtk14">,</span><span class="mtk1">&nbsp;y_train</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 23 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="execute_result output_text"><pre>&lt;qiskit_machine_learning.algorithms.classifiers.vqc.VQC at 0x7eba8adc5220&gt;</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-scnP7k_aHwc4" role="region" aria-label="Cell 24: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk1">predictions&nbsp;=&nbsp;vqc.predict</span><span class="mtk14">(</span><span class="mtk1">X_train</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk1">predictions</span><span class="mtk14">[:</span><span class="mtk6">10</span><span class="mtk14">])</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 24 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>[0 0 1 1 0 1 0 1 0 0]
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-Z0803OSIIAOE" role="region" aria-label="Cell 25: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$091463802$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false" tabindex="-1">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$091463802$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$091463802$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$091463802$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$091463802$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$091463802$--><div class="status">
      <div class="execution-count"><!--?lit$091463802$-->[ ]</div>
      <!--?lit$091463802$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;sklearn.metrics&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;accuracy_score</span></span><br><span><span></span></span><br><span><span class="mtk1">accuracy&nbsp;=&nbsp;accuracy_score</span><span class="mtk14">(</span><span class="mtk1">y_train</span><span class="mtk14">,</span><span class="mtk1">&nbsp;predictions</span><span class="mtk14">)</span></span><br><span><span></span></span><br><span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk5">"Quantum&nbsp;Model&nbsp;Accuracy:"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;accuracy</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$091463802$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 25 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$091463802$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="stream output_text"><pre>Quantum Model Accuracy: 0.84
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" aria-label="Add text cell" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$091463802$-->Text
        </md-outlined-button>
        <!--?lit$091463802$-->
        <!--?lit$091463802$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$091463802$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links" tabindex="-1">
        <!--?lit$091463802$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank" tabindex="-1">
        <!--?lit$091463802$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-scroller>
    </div><div class="right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$091463802$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$091463802$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-2-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button id="tab-pane-2-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$091463802$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$091463802$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$091463802$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-1-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button id="tab-pane-1-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$091463802$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$091463802$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-3-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$091463802$--><md-icon-button id="tab-pane-3-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./MajorProject (3)_files/outputframe(6).html" tabindex="-1" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./MajorProject (3)_files/outputframe(7).html" tabindex="-1" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer-floating-spark><template shadowrootmode="open"><!---->
      <md-icon-button toggle="" id="toggle-composer-button" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false" tabindex="-1">
        <!--?lit$091463802$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$091463802$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$091463802$--><span class="icon"><slot></slot></span>
        <!--?lit$091463802$-->
        <!--?lit$091463802$--><span class="touch"></span>
  </button></template>
        <!--?lit$091463802$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer-button" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template></colab-composer-floating-spark><colab-status-bar role="region" aria-label="Runtime status bar"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="right">
        <!--?lit$091463802$--><colab-execution-status><template shadowrootmode="open"><!----><md-text-button id="execution-status" aria-describedby="execution-status-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template><!--?lit$091463802$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon><!--?lit$091463802$-->1:20 PM</md-text-button>
      <colab-tooltip-trigger aria-hidden="true" id="execution-status-tooltip" for="execution-status" message="Focus the last run cell

1:20 PM (5 hours ago)
executed in 0.014s"><template shadowrootmode="open"><!----><!--?lit$091463802$--><!----><div><!--?lit$091463802$-->Focus the last run cell</div><!----><!----><br><!----><!----><div><!--?lit$091463802$-->1:20 PM (5 hours ago)</div><!----><!----><div><!--?lit$091463802$-->executed in 0.014s</div><!----><!--?--></template>
      </colab-tooltip-trigger></template></colab-execution-status><!--?lit$091463802$--><!--?lit$091463802$--><!--?lit$091463802$--><colab-runtime-status><template shadowrootmode="open"><!----></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->data_object</md-icon>
        <!--?lit$091463802$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$091463802$-->terminal</md-icon>
        <!--?lit$091463802$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 845px; visibility: visible; left: 70px; top: 62px; display: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Locate in Drive<!--?lit$091463802$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Open in playground mode<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->New notebook in Drive<!--?lit$091463802$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Open notebook<!--?lit$091463802$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Upload notebook<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Rename<!--?lit$091463802$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Move<!--?lit$091463802$--></div></div><div command="trash" class="goog-menuitem" role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Move to trash<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class="goog-menuitem" role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Save a copy in Drive<!--?lit$091463802$--></div></div><div command="copy-to-gist" class="goog-menuitem" role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Save a copy as a GitHub Gist<!--?lit$091463802$--></div></div><div command="copy-to-github" class="goog-menuitem" role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Save a copy in GitHub<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class="goog-menuitem" role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Save<!--?lit$091463802$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class="goog-menuitem" role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Save and pin revision<!--?lit$091463802$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class="goog-menuitem" role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Revision history<!--?lit$091463802$--></div></div><div command="show-fileinfo" class="goog-menuitem" role="menuitem" id=":k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Notebook info<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":l" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$091463802$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Print<!--?lit$091463802$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Download .ipynb<!--?lit$091463802$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Download .py<!--?lit$091463802$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Undo<!--?lit$091463802$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Redo<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":t" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Select all cells<!--?lit$091463802$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Cut cell or selection<!--?lit$091463802$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Copy cell or selection<!--?lit$091463802$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Paste<!--?lit$091463802$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Delete selected cells<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":z" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Find and replace<!--?lit$091463802$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Find next<!--?lit$091463802$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":12" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Find previous<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":13" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":14" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Notebook settings<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":15" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":16" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Clear all outputs<!--?lit$091463802$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$091463802$-->Table of contents<!--?lit$091463802$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Executed code history<!--?lit$091463802$--></div></div><div command="start-presentation" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Start slideshow<!--?lit$091463802$--></div></div><div command="start-presentation-beginning" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Start slideshow from beginning<!--?lit$091463802$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$091463802$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1g" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Collapse sections<!--?lit$091463802$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Expand sections<!--?lit$091463802$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Save collapsed section layout<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1k" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Show/hide code<!--?lit$091463802$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Show/hide output<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1n" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Focus next tab<!--?lit$091463802$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Focus previous tab<!--?lit$091463802$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Move tab to next pane<!--?lit$091463802$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Move tab to previous pane<!--?lit$091463802$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Hide comments<!--?lit$091463802$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Minimize comments<!--?lit$091463802$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Expand comments<!--?lit$091463802$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Code cell<!--?lit$091463802$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Text cell<!--?lit$091463802$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Section header cell<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1w" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Scratch code cell<!--?lit$091463802$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Code snippets<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1z" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Add a form field<!--?lit$091463802$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Run all<!--?lit$091463802$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Run before<!--?lit$091463802$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Run the focused cell<!--?lit$091463802$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Run selection<!--?lit$091463802$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Run cell and below<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Interrupt execution<!--?lit$091463802$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Restart session<!--?lit$091463802$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Restart session and run all<!--?lit$091463802$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Disconnect and delete runtime<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Change runtime type<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2e" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Manage sessions<!--?lit$091463802$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->View resources<!--?lit$091463802$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->View runtime logs<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="deploy-cloud-run" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Deploy to Google Cloud Run<!--?lit$091463802$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Command palette<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2m" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Settings<!--?lit$091463802$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Keyboard shortcuts<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2p" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Diff notebooks<!--?lit$091463802$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$091463802$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;" inert="" aria-hidden="true"><!--?lit$091463802$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Frequently asked questions<!--?lit$091463802$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->View release notes<!--?lit$091463802$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Search code snippets<!--?lit$091463802$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2v" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Report a bug<!--?lit$091463802$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Report Drive abuse<!--?lit$091463802$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->Send feedback<!--?lit$091463802$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$091463802$-->View terms of service<!--?lit$091463802$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments" inert="" aria-hidden="true"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button" tabindex="-1">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$091463802$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail" inert="" aria-hidden="true"></div><div class="monaco-aria-container" inert="" aria-hidden="true"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy0d36475035724b5fbf2810b397f43388795b25f80.4050614385" name="apiproxy0d36475035724b5fbf2810b397f43388795b25f80.4050614385" src="./MajorProject (3)_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;" inert=""></iframe><div inert="" aria-hidden="true"><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-s3di4klv0yps" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./MajorProject (3)_files/anchor.html" tabindex="-1"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" tabindex="-1" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe tabindex="-1" style="display: none;" src="./MajorProject (3)_files/saved_resource.html"></iframe></div><iframe src="./MajorProject (3)_files/bscframe.html" style="display: none;" inert="" aria-hidden="true" tabindex="-1"></iframe><mwc-dialog class="auth-github confirm-dialog" open=""><template shadowrootmode="open"><!---->
    <div role="alertdialog" aria-modal="true" aria-describedby="content" class="mdc-dialog mdc-dialog--open" aria-label="Colab is waiting for authorization from GitHub">
      <div class="mdc-dialog__container">
        <div class="mdc-dialog__surface">
          <!--?lit$091463802$-->
      <h2 id="title" class="mdc-dialog__title"><!--?lit$091463802$-->Colab is waiting for authorization from GitHub</h2>
          <div id="content" class="mdc-dialog__content">
            <slot id="contentSlot"></slot>
          </div>
          <footer id="actions" class=" mdc-dialog__actions ">
            <span>
              <slot name="secondaryAction"></slot>
            </span>
            <span>
             <slot name="primaryAction"></slot>
            </span>
          </footer>
        </div>
      </div>
      <div class="mdc-dialog__scrim"></div>
    </div></template><!----><!----><!--?lit$091463802$--><!--?--><!----><!----><!--?lit$091463802$--> <md-text-button slot="primaryAction" dialogaction="ok" dialoginitialfocus="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$091463802$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$091463802$--><button id="button" class="button">
      <!--?lit$091463802$-->
      <span class="touch"></span>
      <!--?lit$091463802$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$091463802$-->
    
    </button>
    </template>
      <!--?lit$091463802$-->Cancel
    </md-text-button><!--?--><!----></mwc-dialog></body></html>