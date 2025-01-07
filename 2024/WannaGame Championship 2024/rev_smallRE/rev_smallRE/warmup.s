	.text
	.file	"warmup.ll"
	.globl	_FE1                            # -- Begin function _FE1
	.p2align	4, 0x90
	.type	_FE1,@function
_FE1:                                   # @_FE1
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movq	%rsi, -16(%rsp)
	movl	$18, -20(%rsp)
	movl	$0, -24(%rsp)
	movl	$3, %eax
	cmpl	$37, -24(%rsp)
	jg	.LBB0_3
	.p2align	4, 0x90
.LBB0_2:                                # =>This Inner Loop Header: Depth=1
	movq	-8(%rsp), %rcx
	movslq	-24(%rsp), %rdx
	movsbl	(%rcx,%rdx), %ecx
	xorl	-20(%rsp), %ecx
	movq	-16(%rsp), %rsi
	movl	%ecx, (%rsi,%rdx,4)
	cmpl	$18, -20(%rsp)
	movl	$18, %ecx
	cmovel	%eax, %ecx
	movl	%ecx, -20(%rsp)
	incl	-24(%rsp)
	cmpl	$37, -24(%rsp)
	jle	.LBB0_2
.LBB0_3:
	retq
.Lfunc_end0:
	.size	_FE1, .Lfunc_end0-_FE1
	.cfi_endproc
                                        # -- End function
	.globl	_FE2                            # -- Begin function _FE2
	.p2align	4, 0x90
	.type	_FE2,@function
_FE2:                                   # @_FE2
	.cfi_startproc
# %bb.0:
	subq	$72, %rsp
	.cfi_def_cfa_offset 80
	movq	%rdi, -88(%rsp)
	movq	%rsi, -96(%rsp)
	movq	%rdx, -104(%rsp)
	movq	%rcx, -112(%rsp)
	movl	$0, -116(%rsp)
	cmpl	$37, -116(%rsp)
	jg	.LBB1_3
	.p2align	4, 0x90
.LBB1_2:                                # =>This Inner Loop Header: Depth=1
	movq	-88(%rsp), %rax
	movq	-96(%rsp), %rcx
	movslq	-116(%rsp), %rdx
	movslq	(%rcx,%rdx,4), %rcx
	movl	(%rax,%rcx,4), %eax
	movl	%eax, -80(%rsp,%rdx,4)
	incl	-116(%rsp)
	cmpl	$37, -116(%rsp)
	jle	.LBB1_2
.LBB1_3:
	movl	$0, -120(%rsp)
	cmpl	$37, -120(%rsp)
	jg	.LBB1_6
	.p2align	4, 0x90
.LBB1_5:                                # =>This Inner Loop Header: Depth=1
	movq	-112(%rsp), %rax
	movslq	-120(%rsp), %rcx
	movslq	-80(%rsp,%rcx,4), %rdx
	movl	(%rax,%rdx,4), %eax
	movq	-104(%rsp), %rdx
	movl	%eax, (%rdx,%rcx,4)
	incl	-120(%rsp)
	cmpl	$37, -120(%rsp)
	jle	.LBB1_5
.LBB1_6:
	addq	$72, %rsp
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	_FE2, .Lfunc_end1-_FE2
	.cfi_endproc
                                        # -- End function
	.globl	_FG                             # -- Begin function _FG
	.p2align	4, 0x90
	.type	_FG,@function
_FG:                                    # @_FG
	.cfi_startproc
# %bb.0:
	movq	%rdi, -24(%rsp)
	movq	%rsi, -8(%rsp)
	movq	%rdx, -16(%rsp)
	movl	$5, -28(%rsp)
	movl	$0, -32(%rsp)
	movl	$18, %eax
	cmpl	$37, -32(%rsp)
	jg	.LBB2_3
	.p2align	4, 0x90
.LBB2_2:                                # =>This Inner Loop Header: Depth=1
	movl	-28(%rsp), %ecx
	movq	-24(%rsp), %rdx
	movslq	-32(%rsp), %rsi
	xorl	%ecx, (%rdx,%rsi,4)
	cmpl	$5, -28(%rsp)
	movl	$5, %ecx
	cmovel	%eax, %ecx
	movl	%ecx, -28(%rsp)
	incl	-32(%rsp)
	cmpl	$37, -32(%rsp)
	jle	.LBB2_2
.LBB2_3:
	movl	$0, -36(%rsp)
	cmpl	$37, -36(%rsp)
	jg	.LBB2_6
	.p2align	4, 0x90
.LBB2_5:                                # =>This Inner Loop Header: Depth=1
	movq	-24(%rsp), %rax
	movslq	-36(%rsp), %rcx
	movl	(%rax,%rcx,4), %eax
	movq	-8(%rsp), %rdx
	addl	(%rdx,%rcx,4), %eax
	movq	-16(%rsp), %rdx
	movl	%eax, (%rdx,%rcx,4)
	incl	-36(%rsp)
	cmpl	$37, -36(%rsp)
	jle	.LBB2_5
.LBB2_6:
	retq
.Lfunc_end2:
	.size	_FG, .Lfunc_end2-_FG
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst16,"aM",@progbits,16
	.p2align	4                               # -- Begin function _FI
.LCPI3_0:
	.quad	0x7fffffffffffffff              # double NaN
	.quad	0x7fffffffffffffff              # double NaN
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3
.LCPI3_1:
	.quad	0x3ddb7cdfd9d7bdbb              # double 1.0E-10
.LCPI3_2:
	.quad	0x3ff0000000000000              # double 1
	.text
	.globl	_FI
	.p2align	4, 0x90
	.type	_FI,@function
_FI:                                    # @_FI
	.cfi_startproc
# %bb.0:
	subq	$23096, %rsp                    # imm = 0x5A38
	.cfi_def_cfa_offset 23104
	movq	%rdi, -24(%rsp)
	movq	%rsi, -32(%rsp)
	movl	$38, -120(%rsp)
	movl	$0, -96(%rsp)
	movsd	.LCPI3_2(%rip), %xmm0           # xmm0 = mem[0],zero
	jmp	.LBB3_1
	.p2align	4, 0x90
.LBB3_10:                               #   in Loop: Header=BB3_1 Depth=1
	incl	-96(%rsp)
.LBB3_1:                                # =>This Loop Header: Depth=1
                                        #     Child Loop BB3_3 Depth 2
                                        #     Child Loop BB3_6 Depth 2
	movl	-96(%rsp), %eax
	cmpl	-120(%rsp), %eax
	jge	.LBB3_11
# %bb.2:                                #   in Loop: Header=BB3_1 Depth=1
	movl	$0, -72(%rsp)
	.p2align	4, 0x90
.LBB3_3:                                #   Parent Loop BB3_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-72(%rsp), %eax
	cmpl	-120(%rsp), %eax
	jge	.LBB3_5
# %bb.4:                                #   in Loop: Header=BB3_3 Depth=2
	movslq	-96(%rsp), %rax
	imulq	$152, %rax, %rcx
	addq	-24(%rsp), %rcx
	movslq	-72(%rsp), %rdx
	xorps	%xmm1, %xmm1
	cvtsi2sdl	(%rcx,%rdx,4), %xmm1
	imulq	$608, %rax, %rax                # imm = 0x260
	leaq	-16(%rsp,%rax), %rax
	movsd	%xmm1, (%rax,%rdx,8)
	incl	-72(%rsp)
	jmp	.LBB3_3
	.p2align	4, 0x90
.LBB3_5:                                #   in Loop: Header=BB3_1 Depth=1
	movl	-120(%rsp), %eax
	movl	%eax, -76(%rsp)
	jmp	.LBB3_6
	.p2align	4, 0x90
.LBB3_9:                                #   in Loop: Header=BB3_6 Depth=2
	imulq	$608, %rax, %rax                # imm = 0x260
	leaq	-16(%rsp,%rax), %rax
	movsd	%xmm1, (%rax,%rcx,8)
	incl	-76(%rsp)
.LBB3_6:                                #   Parent Loop BB3_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-120(%rsp), %eax
	addl	%eax, %eax
	cmpl	%eax, -76(%rsp)
	jge	.LBB3_10
# %bb.7:                                #   in Loop: Header=BB3_6 Depth=2
	movslq	-96(%rsp), %rax
	movslq	-76(%rsp), %rcx
	movl	-120(%rsp), %edx
	movl	%ecx, %esi
	subl	%edx, %esi
	cmpl	%esi, %eax
	movapd	%xmm0, %xmm1
	je	.LBB3_9
# %bb.8:                                #   in Loop: Header=BB3_6 Depth=2
	xorpd	%xmm1, %xmm1
	jmp	.LBB3_9
.LBB3_11:
	movl	$0, -116(%rsp)
	movapd	.LCPI3_0(%rip), %xmm0           # xmm0 = [NaN,NaN]
	movsd	.LCPI3_1(%rip), %xmm1           # xmm1 = mem[0],zero
	jmp	.LBB3_12
	.p2align	4, 0x90
.LBB3_36:                               #   in Loop: Header=BB3_12 Depth=1
	incl	-116(%rsp)
.LBB3_12:                               # =>This Loop Header: Depth=1
                                        #     Child Loop BB3_15 Depth 2
                                        #     Child Loop BB3_23 Depth 2
                                        #     Child Loop BB3_27 Depth 2
                                        #     Child Loop BB3_30 Depth 2
                                        #       Child Loop BB3_33 Depth 3
	movl	-116(%rsp), %eax
	cmpl	-120(%rsp), %eax
	jge	.LBB3_37
# %bb.13:                               #   in Loop: Header=BB3_12 Depth=1
	movslq	-116(%rsp), %rax
	imulq	$608, %rax, %rcx                # imm = 0x260
	leaq	-16(%rsp,%rcx), %rcx
	movsd	(%rcx,%rax,8), %xmm2            # xmm2 = mem[0],zero
	movsd	%xmm2, -56(%rsp)
	andpd	%xmm0, %xmm2
	ucomisd	%xmm2, %xmm1
	jbe	.LBB3_26
# %bb.14:                               #   in Loop: Header=BB3_12 Depth=1
	movl	-116(%rsp), %eax
	movl	%eax, -100(%rsp)
	movsd	-56(%rsp), %xmm2                # xmm2 = mem[0],zero
	andpd	%xmm0, %xmm2
	movlpd	%xmm2, -64(%rsp)
	incl	%eax
	movl	%eax, -104(%rsp)
	jmp	.LBB3_15
	.p2align	4, 0x90
.LBB3_18:                               #   in Loop: Header=BB3_15 Depth=2
	incl	-104(%rsp)
.LBB3_15:                               #   Parent Loop BB3_12 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-104(%rsp), %eax
	cmpl	-120(%rsp), %eax
	jge	.LBB3_19
# %bb.16:                               #   in Loop: Header=BB3_15 Depth=2
	movslq	-104(%rsp), %rax
	imulq	$608, %rax, %rax                # imm = 0x260
	leaq	-16(%rsp,%rax), %rax
	movslq	-116(%rsp), %rcx
	movsd	(%rax,%rcx,8), %xmm2            # xmm2 = mem[0],zero
	andpd	%xmm0, %xmm2
	ucomisd	-64(%rsp), %xmm2
	jbe	.LBB3_18
# %bb.17:                               #   in Loop: Header=BB3_15 Depth=2
	movslq	-104(%rsp), %rax
	imulq	$608, %rax, %rcx                # imm = 0x260
	leaq	-16(%rsp,%rcx), %rcx
	movslq	-116(%rsp), %rdx
	movsd	(%rcx,%rdx,8), %xmm2            # xmm2 = mem[0],zero
	andpd	%xmm0, %xmm2
	movlpd	%xmm2, -64(%rsp)
	movl	%eax, -100(%rsp)
	jmp	.LBB3_18
	.p2align	4, 0x90
.LBB3_19:                               #   in Loop: Header=BB3_12 Depth=1
	movl	-100(%rsp), %eax
	cmpl	-116(%rsp), %eax
	je	.LBB3_21
# %bb.20:                               #   in Loop: Header=BB3_12 Depth=1
	movsd	-64(%rsp), %xmm2                # xmm2 = mem[0],zero
	andpd	%xmm0, %xmm2
	ucomisd	%xmm2, %xmm1
	ja	.LBB3_21
# %bb.22:                               #   in Loop: Header=BB3_12 Depth=1
	movl	$0, -108(%rsp)
	.p2align	4, 0x90
.LBB3_23:                               #   Parent Loop BB3_12 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-120(%rsp), %eax
	addl	%eax, %eax
	cmpl	%eax, -108(%rsp)
	jge	.LBB3_25
# %bb.24:                               #   in Loop: Header=BB3_23 Depth=2
	movslq	-108(%rsp), %rax
	movslq	-116(%rsp), %rcx
	imulq	$608, %rcx, %rcx                # imm = 0x260
	leaq	-16(%rsp,%rcx), %rcx
	movsd	(%rcx,%rax,8), %xmm2            # xmm2 = mem[0],zero
	movsd	%xmm2, -40(%rsp)
	movslq	-100(%rsp), %rdx
	imulq	$608, %rdx, %rdx                # imm = 0x260
	leaq	-16(%rsp,%rdx), %rdx
	movsd	(%rdx,%rax,8), %xmm2            # xmm2 = mem[0],zero
	movsd	%xmm2, (%rcx,%rax,8)
	movsd	-40(%rsp), %xmm2                # xmm2 = mem[0],zero
	movslq	-100(%rsp), %rax
	imulq	$608, %rax, %rax                # imm = 0x260
	leaq	-16(%rsp,%rax), %rax
	movslq	-108(%rsp), %rcx
	movsd	%xmm2, (%rax,%rcx,8)
	incl	-108(%rsp)
	jmp	.LBB3_23
	.p2align	4, 0x90
.LBB3_25:                               #   in Loop: Header=BB3_12 Depth=1
	movslq	-116(%rsp), %rax
	imulq	$608, %rax, %rcx                # imm = 0x260
	leaq	-16(%rsp,%rcx), %rcx
	movsd	(%rcx,%rax,8), %xmm2            # xmm2 = mem[0],zero
	movsd	%xmm2, -56(%rsp)
.LBB3_26:                               #   in Loop: Header=BB3_12 Depth=1
	movl	$0, -80(%rsp)
	.p2align	4, 0x90
.LBB3_27:                               #   Parent Loop BB3_12 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-120(%rsp), %eax
	addl	%eax, %eax
	cmpl	%eax, -80(%rsp)
	jge	.LBB3_29
# %bb.28:                               #   in Loop: Header=BB3_27 Depth=2
	movslq	-116(%rsp), %rax
	imulq	$608, %rax, %rax                # imm = 0x260
	leaq	-16(%rsp,%rax), %rax
	movslq	-80(%rsp), %rcx
	movsd	(%rax,%rcx,8), %xmm2            # xmm2 = mem[0],zero
	divsd	-56(%rsp), %xmm2
	movsd	%xmm2, (%rax,%rcx,8)
	incl	-80(%rsp)
	jmp	.LBB3_27
	.p2align	4, 0x90
.LBB3_29:                               #   in Loop: Header=BB3_12 Depth=1
	movl	$0, -112(%rsp)
	jmp	.LBB3_30
	.p2align	4, 0x90
.LBB3_35:                               #   in Loop: Header=BB3_30 Depth=2
	incl	-112(%rsp)
.LBB3_30:                               #   Parent Loop BB3_12 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB3_33 Depth 3
	movl	-112(%rsp), %eax
	cmpl	-120(%rsp), %eax
	jge	.LBB3_36
# %bb.31:                               #   in Loop: Header=BB3_30 Depth=2
	movl	-116(%rsp), %eax
	cmpl	-112(%rsp), %eax
	je	.LBB3_35
# %bb.32:                               #   in Loop: Header=BB3_30 Depth=2
	movslq	-112(%rsp), %rax
	imulq	$608, %rax, %rax                # imm = 0x260
	leaq	-16(%rsp,%rax), %rax
	movslq	-116(%rsp), %rcx
	movsd	(%rax,%rcx,8), %xmm2            # xmm2 = mem[0],zero
	movsd	%xmm2, -48(%rsp)
	movl	$0, -84(%rsp)
	.p2align	4, 0x90
.LBB3_33:                               #   Parent Loop BB3_12 Depth=1
                                        #     Parent Loop BB3_30 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-120(%rsp), %eax
	addl	%eax, %eax
	cmpl	%eax, -84(%rsp)
	jge	.LBB3_35
# %bb.34:                               #   in Loop: Header=BB3_33 Depth=3
	movsd	-48(%rsp), %xmm2                # xmm2 = mem[0],zero
	movslq	-116(%rsp), %rax
	imulq	$608, %rax, %rax                # imm = 0x260
	leaq	-16(%rsp,%rax), %rax
	movslq	-84(%rsp), %rcx
	movslq	-112(%rsp), %rdx
	imulq	$608, %rdx, %rdx                # imm = 0x260
	leaq	-16(%rsp,%rdx), %rdx
	movsd	(%rdx,%rcx,8), %xmm3            # xmm3 = mem[0],zero
	mulsd	(%rax,%rcx,8), %xmm2
	subsd	%xmm2, %xmm3
	movsd	%xmm3, (%rdx,%rcx,8)
	incl	-84(%rsp)
	jmp	.LBB3_33
.LBB3_37:
	movl	$0, -88(%rsp)
	jmp	.LBB3_38
	.p2align	4, 0x90
.LBB3_42:                               #   in Loop: Header=BB3_38 Depth=1
	incl	-88(%rsp)
.LBB3_38:                               # =>This Loop Header: Depth=1
                                        #     Child Loop BB3_40 Depth 2
	movl	-88(%rsp), %eax
	cmpl	-120(%rsp), %eax
	jge	.LBB3_43
# %bb.39:                               #   in Loop: Header=BB3_38 Depth=1
	movl	$0, -92(%rsp)
	.p2align	4, 0x90
.LBB3_40:                               #   Parent Loop BB3_38 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-92(%rsp), %eax
	cmpl	-120(%rsp), %eax
	jge	.LBB3_42
# %bb.41:                               #   in Loop: Header=BB3_40 Depth=2
	movslq	-88(%rsp), %rax
	imulq	$608, %rax, %rcx                # imm = 0x260
	leaq	-16(%rsp,%rcx), %rcx
	movslq	-92(%rsp), %rdx
	movslq	-120(%rsp), %rsi
	addq	%rdx, %rsi
	movsd	(%rcx,%rsi,8), %xmm0            # xmm0 = mem[0],zero
	imulq	$304, %rax, %rax                # imm = 0x130
	addq	-32(%rsp), %rax
	movsd	%xmm0, (%rax,%rdx,8)
	incl	-92(%rsp)
	jmp	.LBB3_40
.LBB3_21:
	movl	$0, -68(%rsp)
	jmp	.LBB3_44
.LBB3_43:
	movl	$1, -68(%rsp)
.LBB3_44:
	movl	-68(%rsp), %eax
	addq	$23096, %rsp                    # imm = 0x5A38
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end3:
	.size	_FI, .Lfunc_end3-_FI
	.cfi_endproc
                                        # -- End function
	.globl	_FM                             # -- Begin function _FM
	.p2align	4, 0x90
	.type	_FM,@function
_FM:                                    # @_FM
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movq	%rsi, -16(%rsp)
	movq	%rdx, -24(%rsp)
	movl	$0, -32(%rsp)
	jmp	.LBB4_1
	.p2align	4, 0x90
.LBB4_5:                                #   in Loop: Header=BB4_1 Depth=1
	incl	-32(%rsp)
.LBB4_1:                                # =>This Loop Header: Depth=1
                                        #     Child Loop BB4_4 Depth 2
	cmpl	$37, -32(%rsp)
	jg	.LBB4_6
# %bb.2:                                #   in Loop: Header=BB4_1 Depth=1
	movq	-24(%rsp), %rax
	movslq	-32(%rsp), %rcx
	movq	$0, (%rax,%rcx,8)
	movl	$0, -28(%rsp)
	cmpl	$37, -28(%rsp)
	jg	.LBB4_5
	.p2align	4, 0x90
.LBB4_4:                                #   Parent Loop BB4_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movq	-8(%rsp), %rax
	movslq	-28(%rsp), %rcx
	xorps	%xmm0, %xmm0
	cvtsi2sdl	(%rax,%rcx,4), %xmm0
	imulq	$304, %rcx, %rax                # imm = 0x130
	addq	-16(%rsp), %rax
	movslq	-32(%rsp), %rcx
	movq	-24(%rsp), %rdx
	mulsd	(%rax,%rcx,8), %xmm0
	addsd	(%rdx,%rcx,8), %xmm0
	movsd	%xmm0, (%rdx,%rcx,8)
	incl	-28(%rsp)
	cmpl	$37, -28(%rsp)
	jle	.LBB4_4
	jmp	.LBB4_5
.LBB4_6:
	retq
.Lfunc_end4:
	.size	_FM, .Lfunc_end4-_FM
	.cfi_endproc
                                        # -- End function
	.globl	CHK                             # -- Begin function CHK
	.p2align	4, 0x90
	.type	CHK,@function
CHK:                                    # @CHK
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movl	$0, -16(%rsp)
	cmpl	$37, -16(%rsp)
	jg	.LBB5_5
	.p2align	4, 0x90
.LBB5_2:                                # =>This Inner Loop Header: Depth=1
	movq	-8(%rsp), %rax
	movslq	-16(%rsp), %rcx
	movl	(%rax,%rcx,4), %eax
	cmpl	final(,%rcx,4), %eax
	jne	.LBB5_3
# %bb.4:                                #   in Loop: Header=BB5_2 Depth=1
	incl	-16(%rsp)
	cmpl	$37, -16(%rsp)
	jle	.LBB5_2
.LBB5_5:
	movl	$1, -12(%rsp)
	movl	-12(%rsp), %eax
	retq
.LBB5_3:
	movl	$0, -12(%rsp)
	movl	-12(%rsp), %eax
	retq
.Lfunc_end5:
	.size	CHK, .Lfunc_end5-CHK
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3                               # -- Begin function init
.LCPI6_0:
	.quad	0x3fe0000000000000              # double 0.5
	.text
	.globl	init
	.p2align	4, 0x90
	.type	init,@function
init:                                   # @init
	.cfi_startproc
# %bb.0:
	pushq	%r15
	.cfi_def_cfa_offset 16
	pushq	%r14
	.cfi_def_cfa_offset 24
	pushq	%r12
	.cfi_def_cfa_offset 32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	subq	$19688, %rsp                    # imm = 0x4CE8
	.cfi_def_cfa_offset 19728
	.cfi_offset %rbx, -40
	.cfi_offset %r12, -32
	.cfi_offset %r14, -24
	.cfi_offset %r15, -16
	leaq	2352(%rsp), %r14
	movl	$.L__const.init.var2, %esi
	movl	$5776, %edx                     # imm = 0x1690
	movq	%r14, %rdi
	callq	memcpy@PLT
	leaq	1328(%rsp), %rdi
	movl	$.L__const.init.sbox, %esi
	movl	$1024, %edx                     # imm = 0x400
	callq	memcpy@PLT
	leaq	1168(%rsp), %r15
	movl	$.L__const.init.var1, %esi
	movl	$152, %edx
	movq	%r15, %rdi
	callq	memcpy@PLT
	leaq	1008(%rsp), %rbx
	movl	$.L__const.init.var6, %esi
	movl	$152, %edx
	movq	%rbx, %rdi
	callq	memcpy@PLT
	leaq	848(%rsp), %r12
	movq	%r15, %rdi
	movq	%rbx, %rsi
	movq	%r12, %rdx
	callq	_FG
	leaq	8128(%rsp), %rbx
	movq	%r14, %rdi
	movq	%rbx, %rsi
	callq	_FI
	leaq	544(%rsp), %rdx
	movq	%r12, %rdi
	movq	%rbx, %rsi
	callq	_FM
	movl	$0, 12(%rsp)
	movsd	.LCPI6_0(%rip), %xmm0           # xmm0 = mem[0],zero
	cmpl	$37, 12(%rsp)
	jg	.LBB6_3
	.p2align	4, 0x90
.LBB6_2:                                # =>This Inner Loop Header: Depth=1
	movslq	12(%rsp), %rax
	movsd	544(%rsp,%rax,8), %xmm1         # xmm1 = mem[0],zero
	addsd	%xmm0, %xmm1
	cvttsd2si	%xmm1, %ecx
	movl	%ecx, 64(%rsp,%rax,4)
	incl	%eax
	movl	%eax, 12(%rsp)
	cmpl	$37, 12(%rsp)
	jle	.LBB6_2
.LBB6_3:
	movl	$.L.str.2, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	movq	stdin@GOTPCREL(%rip), %rax
	movq	(%rax), %rdx
	leaq	16(%rsp), %rbx
	movq	%rbx, %rdi
	movl	$39, %esi
	callq	fgets@PLT
	leaq	384(%rsp), %r14
	movq	%rbx, %rdi
	movq	%r14, %rsi
	callq	_FE1
	leaq	64(%rsp), %rsi
	leaq	224(%rsp), %rbx
	leaq	1328(%rsp), %rcx
	movq	%r14, %rdi
	movq	%rbx, %rdx
	callq	_FE2
	movq	%rbx, %rdi
	callq	CHK
	testl	%eax, %eax
	je	.LBB6_5
# %bb.4:
	movq	final2(%rip), %rsi
	jmp	.LBB6_6
.LBB6_5:
	movq	final1(%rip), %rsi
.LBB6_6:
	movl	$.L.str.3, %edi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	addq	$19688, %rsp                    # imm = 0x4CE8
	.cfi_def_cfa_offset 40
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%r12
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end6:
	.size	init, .Lfunc_end6-init
	.cfi_endproc
                                        # -- End function
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	pushq	%rax
	.cfi_def_cfa_offset 16
	callq	init
	movl	$.L.str.4, %edi
	callq	puts@PLT
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end7:
	.size	main, .Lfunc_end7-main
	.cfi_endproc
                                        # -- End function
	.type	final,@object                   # @final
	.section	.rodata,"a",@progbits
	.globl	final
	.p2align	4
final:
	.long	160                             # 0xa0
	.long	24                              # 0x18
	.long	64                              # 0x40
	.long	211                             # 0xd3
	.long	111                             # 0x6f
	.long	150                             # 0x96
	.long	7                               # 0x7
	.long	35                              # 0x23
	.long	197                             # 0xc5
	.long	107                             # 0x6b
	.long	12                              # 0xc
	.long	26                              # 0x1a
	.long	107                             # 0x6b
	.long	210                             # 0xd2
	.long	210                             # 0xd2
	.long	35                              # 0x23
	.long	21                              # 0x15
	.long	49                              # 0x31
	.long	2                               # 0x2
	.long	136                             # 0x88
	.long	35                              # 0x23
	.long	131                             # 0x83
	.long	197                             # 0xc5
	.long	35                              # 0x23
	.long	62                              # 0x3e
	.long	35                              # 0x23
	.long	126                             # 0x7e
	.long	19                              # 0x13
	.long	62                              # 0x3e
	.long	44                              # 0x2c
	.long	72                              # 0x48
	.long	197                             # 0xc5
	.long	185                             # 0xb9
	.long	158                             # 0x9e
	.long	13                              # 0xd
	.long	10                              # 0xa
	.long	7                               # 0x7
	.long	89                              # 0x59
	.size	final, 152

	.type	.L.str,@object                  # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"aHR0cDovL3N1cmwubGkvcHdhbG9u"
	.size	.L.str, 29

	.type	final1,@object                  # @final1
	.data
	.globl	final1
	.p2align	3
final1:
	.quad	.L.str
	.size	final1, 8

	.type	.L.str.1,@object                # @.str.1
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str.1:
	.asciz	"Q29uZ3JhdHMhISEhISEgZ28gZ28gZ28gc3VibWl0IGZsYWcgZ28gZ28gZ28="
	.size	.L.str.1, 61

	.type	final2,@object                  # @final2
	.data
	.globl	final2
	.p2align	3
final2:
	.quad	.L.str.1
	.size	final2, 8

	.type	.L__const.init.var2,@object     # @__const.init.var2
	.section	.rodata,"a",@progbits
	.p2align	4
.L__const.init.var2:
	.long	75                              # 0x4b
	.long	21                              # 0x15
	.long	68                              # 0x44
	.long	57                              # 0x39
	.long	32                              # 0x20
	.long	14                              # 0xe
	.long	5                               # 0x5
	.long	29                              # 0x1d
	.long	67                              # 0x43
	.long	70                              # 0x46
	.long	89                              # 0x59
	.long	3                               # 0x3
	.long	51                              # 0x33
	.long	74                              # 0x4a
	.long	12                              # 0xc
	.long	5                               # 0x5
	.long	29                              # 0x1d
	.long	19                              # 0x13
	.long	46                              # 0x2e
	.long	44                              # 0x2c
	.long	25                              # 0x19
	.long	23                              # 0x17
	.long	50                              # 0x32
	.long	82                              # 0x52
	.long	62                              # 0x3e
	.long	17                              # 0x11
	.long	67                              # 0x43
	.long	57                              # 0x39
	.long	34                              # 0x22
	.long	45                              # 0x2d
	.long	82                              # 0x52
	.long	16                              # 0x10
	.long	32                              # 0x20
	.long	97                              # 0x61
	.long	68                              # 0x44
	.long	43                              # 0x2b
	.long	94                              # 0x5e
	.long	56                              # 0x38
	.long	16                              # 0x10
	.long	54                              # 0x36
	.long	45                              # 0x2d
	.long	90                              # 0x5a
	.long	15                              # 0xf
	.long	62                              # 0x3e
	.long	48                              # 0x30
	.long	30                              # 0x1e
	.long	62                              # 0x3e
	.long	31                              # 0x1f
	.long	87                              # 0x57
	.long	81                              # 0x51
	.long	54                              # 0x36
	.long	73                              # 0x49
	.long	79                              # 0x4f
	.long	70                              # 0x46
	.long	75                              # 0x4b
	.long	89                              # 0x59
	.long	81                              # 0x51
	.long	32                              # 0x20
	.long	25                              # 0x19
	.long	50                              # 0x32
	.long	50                              # 0x32
	.long	75                              # 0x4b
	.long	54                              # 0x36
	.long	14                              # 0xe
	.long	22                              # 0x16
	.long	39                              # 0x27
	.long	55                              # 0x37
	.long	75                              # 0x4b
	.long	53                              # 0x35
	.long	87                              # 0x57
	.long	0                               # 0x0
	.long	68                              # 0x44
	.long	32                              # 0x20
	.long	94                              # 0x5e
	.long	83                              # 0x53
	.long	33                              # 0x21
	.long	3                               # 0x3
	.long	92                              # 0x5c
	.long	93                              # 0x5d
	.long	5                               # 0x5
	.long	48                              # 0x30
	.long	98                              # 0x62
	.long	86                              # 0x56
	.long	65                              # 0x41
	.long	68                              # 0x44
	.long	49                              # 0x31
	.long	57                              # 0x39
	.long	67                              # 0x43
	.long	45                              # 0x2d
	.long	66                              # 0x42
	.long	36                              # 0x24
	.long	21                              # 0x15
	.long	23                              # 0x17
	.long	13                              # 0xd
	.long	30                              # 0x1e
	.long	91                              # 0x5b
	.long	79                              # 0x4f
	.long	73                              # 0x49
	.long	24                              # 0x18
	.long	43                              # 0x2b
	.long	21                              # 0x15
	.long	36                              # 0x24
	.long	54                              # 0x36
	.long	95                              # 0x5f
	.long	31                              # 0x1f
	.long	74                              # 0x4a
	.long	81                              # 0x51
	.long	37                              # 0x25
	.long	31                              # 0x1f
	.long	19                              # 0x13
	.long	44                              # 0x2c
	.long	80                              # 0x50
	.long	80                              # 0x50
	.long	17                              # 0x11
	.long	14                              # 0xe
	.long	62                              # 0x3e
	.long	1                               # 0x1
	.long	54                              # 0x36
	.long	32                              # 0x20
	.long	90                              # 0x5a
	.long	27                              # 0x1b
	.long	66                              # 0x42
	.long	89                              # 0x59
	.long	68                              # 0x44
	.long	4                               # 0x4
	.long	97                              # 0x61
	.long	32                              # 0x20
	.long	1                               # 0x1
	.long	71                              # 0x47
	.long	80                              # 0x50
	.long	2                               # 0x2
	.long	29                              # 0x1d
	.long	89                              # 0x59
	.long	1                               # 0x1
	.long	78                              # 0x4e
	.long	71                              # 0x47
	.long	12                              # 0xc
	.long	31                              # 0x1f
	.long	2                               # 0x2
	.long	79                              # 0x4f
	.long	62                              # 0x3e
	.long	34                              # 0x22
	.long	15                              # 0xf
	.long	22                              # 0x16
	.long	55                              # 0x37
	.long	1                               # 0x1
	.long	29                              # 0x1d
	.long	51                              # 0x33
	.long	57                              # 0x39
	.long	51                              # 0x33
	.long	52                              # 0x34
	.long	52                              # 0x34
	.long	60                              # 0x3c
	.long	27                              # 0x1b
	.long	21                              # 0x15
	.long	64                              # 0x40
	.long	83                              # 0x53
	.long	70                              # 0x46
	.long	40                              # 0x28
	.long	42                              # 0x2a
	.long	18                              # 0x12
	.long	99                              # 0x63
	.long	76                              # 0x4c
	.long	26                              # 0x1a
	.long	28                              # 0x1c
	.long	3                               # 0x3
	.long	94                              # 0x5e
	.long	22                              # 0x16
	.long	6                               # 0x6
	.long	42                              # 0x2a
	.long	31                              # 0x1f
	.long	21                              # 0x15
	.long	72                              # 0x48
	.long	71                              # 0x47
	.long	43                              # 0x2b
	.long	84                              # 0x54
	.long	60                              # 0x3c
	.long	44                              # 0x2c
	.long	5                               # 0x5
	.long	74                              # 0x4a
	.long	24                              # 0x18
	.long	42                              # 0x2a
	.long	16                              # 0x10
	.long	95                              # 0x5f
	.long	34                              # 0x22
	.long	50                              # 0x32
	.long	51                              # 0x33
	.long	36                              # 0x24
	.long	39                              # 0x27
	.long	49                              # 0x31
	.long	38                              # 0x26
	.long	9                               # 0x9
	.long	65                              # 0x41
	.long	33                              # 0x21
	.long	48                              # 0x30
	.long	47                              # 0x2f
	.long	89                              # 0x59
	.long	33                              # 0x21
	.long	6                               # 0x6
	.long	75                              # 0x4b
	.long	76                              # 0x4c
	.long	62                              # 0x3e
	.long	44                              # 0x2c
	.long	83                              # 0x53
	.long	82                              # 0x52
	.long	2                               # 0x2
	.long	21                              # 0x15
	.long	95                              # 0x5f
	.long	58                              # 0x3a
	.long	96                              # 0x60
	.long	71                              # 0x47
	.long	20                              # 0x14
	.long	2                               # 0x2
	.long	7                               # 0x7
	.long	82                              # 0x52
	.long	47                              # 0x2f
	.long	21                              # 0x15
	.long	95                              # 0x5f
	.long	97                              # 0x61
	.long	77                              # 0x4d
	.long	7                               # 0x7
	.long	73                              # 0x49
	.long	98                              # 0x62
	.long	2                               # 0x2
	.long	33                              # 0x21
	.long	48                              # 0x30
	.long	58                              # 0x3a
	.long	79                              # 0x4f
	.long	32                              # 0x20
	.long	98                              # 0x62
	.long	34                              # 0x22
	.long	29                              # 0x1d
	.long	33                              # 0x21
	.long	87                              # 0x57
	.long	24                              # 0x18
	.long	70                              # 0x46
	.long	44                              # 0x2c
	.long	54                              # 0x36
	.long	64                              # 0x40
	.long	17                              # 0x11
	.long	10                              # 0xa
	.long	85                              # 0x55
	.long	24                              # 0x18
	.long	49                              # 0x31
	.long	55                              # 0x37
	.long	31                              # 0x1f
	.long	37                              # 0x25
	.long	54                              # 0x36
	.long	73                              # 0x49
	.long	41                              # 0x29
	.long	14                              # 0xe
	.long	2                               # 0x2
	.long	15                              # 0xf
	.long	87                              # 0x57
	.long	94                              # 0x5e
	.long	96                              # 0x60
	.long	48                              # 0x30
	.long	2                               # 0x2
	.long	21                              # 0x15
	.long	53                              # 0x35
	.long	36                              # 0x24
	.long	99                              # 0x63
	.long	64                              # 0x40
	.long	27                              # 0x1b
	.long	42                              # 0x2a
	.long	46                              # 0x2e
	.long	53                              # 0x35
	.long	71                              # 0x47
	.long	21                              # 0x15
	.long	93                              # 0x5d
	.long	16                              # 0x10
	.long	29                              # 0x1d
	.long	40                              # 0x28
	.long	1                               # 0x1
	.long	23                              # 0x17
	.long	22                              # 0x16
	.long	60                              # 0x3c
	.long	45                              # 0x2d
	.long	37                              # 0x25
	.long	88                              # 0x58
	.long	58                              # 0x3a
	.long	51                              # 0x33
	.long	85                              # 0x55
	.long	19                              # 0x13
	.long	30                              # 0x1e
	.long	7                               # 0x7
	.long	46                              # 0x2e
	.long	9                               # 0x9
	.long	85                              # 0x55
	.long	28                              # 0x1c
	.long	48                              # 0x30
	.long	35                              # 0x23
	.long	21                              # 0x15
	.long	57                              # 0x39
	.long	96                              # 0x60
	.long	80                              # 0x50
	.long	17                              # 0x11
	.long	90                              # 0x5a
	.long	99                              # 0x63
	.long	64                              # 0x40
	.long	87                              # 0x57
	.long	35                              # 0x23
	.long	5                               # 0x5
	.long	29                              # 0x1d
	.long	64                              # 0x40
	.long	91                              # 0x5b
	.long	38                              # 0x26
	.long	41                              # 0x29
	.long	44                              # 0x2c
	.long	60                              # 0x3c
	.long	14                              # 0xe
	.long	90                              # 0x5a
	.long	45                              # 0x2d
	.long	48                              # 0x30
	.long	10                              # 0xa
	.long	50                              # 0x32
	.long	46                              # 0x2e
	.long	4                               # 0x4
	.long	35                              # 0x23
	.long	84                              # 0x54
	.long	17                              # 0x11
	.long	55                              # 0x37
	.long	94                              # 0x5e
	.long	60                              # 0x3c
	.long	41                              # 0x29
	.long	12                              # 0xc
	.long	34                              # 0x22
	.long	60                              # 0x3c
	.long	21                              # 0x15
	.long	11                              # 0xb
	.long	66                              # 0x42
	.long	9                               # 0x9
	.long	89                              # 0x59
	.long	71                              # 0x47
	.long	52                              # 0x34
	.long	70                              # 0x46
	.long	66                              # 0x42
	.long	35                              # 0x23
	.long	92                              # 0x5c
	.long	92                              # 0x5c
	.long	37                              # 0x25
	.long	34                              # 0x22
	.long	96                              # 0x60
	.long	71                              # 0x47
	.long	82                              # 0x52
	.long	17                              # 0x11
	.long	91                              # 0x5b
	.long	64                              # 0x40
	.long	64                              # 0x40
	.long	99                              # 0x63
	.long	71                              # 0x47
	.long	76                              # 0x4c
	.long	84                              # 0x54
	.long	40                              # 0x28
	.long	3                               # 0x3
	.long	91                              # 0x5b
	.long	97                              # 0x61
	.long	47                              # 0x2f
	.long	96                              # 0x60
	.long	20                              # 0x14
	.long	98                              # 0x62
	.long	60                              # 0x3c
	.long	52                              # 0x34
	.long	38                              # 0x26
	.long	51                              # 0x33
	.long	92                              # 0x5c
	.long	99                              # 0x63
	.long	27                              # 0x1b
	.long	24                              # 0x18
	.long	38                              # 0x26
	.long	4                               # 0x4
	.long	52                              # 0x34
	.long	87                              # 0x57
	.long	20                              # 0x14
	.long	5                               # 0x5
	.long	82                              # 0x52
	.long	66                              # 0x42
	.long	27                              # 0x1b
	.long	30                              # 0x1e
	.long	22                              # 0x16
	.long	28                              # 0x1c
	.long	22                              # 0x16
	.long	98                              # 0x62
	.long	9                               # 0x9
	.long	19                              # 0x13
	.long	99                              # 0x63
	.long	40                              # 0x28
	.long	97                              # 0x61
	.long	70                              # 0x46
	.long	34                              # 0x22
	.long	31                              # 0x1f
	.long	95                              # 0x5f
	.long	40                              # 0x28
	.long	46                              # 0x2e
	.long	81                              # 0x51
	.long	5                               # 0x5
	.long	44                              # 0x2c
	.long	43                              # 0x2b
	.long	40                              # 0x28
	.long	41                              # 0x29
	.long	20                              # 0x14
	.long	44                              # 0x2c
	.long	24                              # 0x18
	.long	22                              # 0x16
	.long	12                              # 0xc
	.long	71                              # 0x47
	.long	92                              # 0x5c
	.long	33                              # 0x21
	.long	80                              # 0x50
	.long	97                              # 0x61
	.long	53                              # 0x35
	.long	8                               # 0x8
	.long	19                              # 0x13
	.long	5                               # 0x5
	.long	45                              # 0x2d
	.long	12                              # 0xc
	.long	77                              # 0x4d
	.long	15                              # 0xf
	.long	40                              # 0x28
	.long	31                              # 0x1f
	.long	89                              # 0x59
	.long	5                               # 0x5
	.long	1                               # 0x1
	.long	5                               # 0x5
	.long	99                              # 0x63
	.long	48                              # 0x30
	.long	13                              # 0xd
	.long	44                              # 0x2c
	.long	93                              # 0x5d
	.long	37                              # 0x25
	.long	81                              # 0x51
	.long	7                               # 0x7
	.long	58                              # 0x3a
	.long	85                              # 0x55
	.long	44                              # 0x2c
	.long	87                              # 0x57
	.long	50                              # 0x32
	.long	12                              # 0xc
	.long	46                              # 0x2e
	.long	47                              # 0x2f
	.long	80                              # 0x50
	.long	48                              # 0x30
	.long	69                              # 0x45
	.long	7                               # 0x7
	.long	20                              # 0x14
	.long	4                               # 0x4
	.long	48                              # 0x30
	.long	79                              # 0x4f
	.long	24                              # 0x18
	.long	73                              # 0x49
	.long	79                              # 0x4f
	.long	39                              # 0x27
	.long	89                              # 0x59
	.long	21                              # 0x15
	.long	40                              # 0x28
	.long	13                              # 0xd
	.long	24                              # 0x18
	.long	7                               # 0x7
	.long	24                              # 0x18
	.long	19                              # 0x13
	.long	1                               # 0x1
	.long	26                              # 0x1a
	.long	59                              # 0x3b
	.long	11                              # 0xb
	.long	75                              # 0x4b
	.long	93                              # 0x5d
	.long	20                              # 0x14
	.long	18                              # 0x12
	.long	71                              # 0x47
	.long	1                               # 0x1
	.long	22                              # 0x16
	.long	92                              # 0x5c
	.long	72                              # 0x48
	.long	44                              # 0x2c
	.long	79                              # 0x4f
	.long	40                              # 0x28
	.long	63                              # 0x3f
	.long	70                              # 0x46
	.long	34                              # 0x22
	.long	20                              # 0x14
	.long	45                              # 0x2d
	.long	24                              # 0x18
	.long	91                              # 0x5b
	.long	52                              # 0x34
	.long	2                               # 0x2
	.long	26                              # 0x1a
	.long	20                              # 0x14
	.long	0                               # 0x0
	.long	9                               # 0x9
	.long	16                              # 0x10
	.long	33                              # 0x21
	.long	89                              # 0x59
	.long	96                              # 0x60
	.long	62                              # 0x3e
	.long	95                              # 0x5f
	.long	26                              # 0x1a
	.long	19                              # 0x13
	.long	59                              # 0x3b
	.long	22                              # 0x16
	.long	24                              # 0x18
	.long	42                              # 0x2a
	.long	18                              # 0x12
	.long	9                               # 0x9
	.long	81                              # 0x51
	.long	3                               # 0x3
	.long	6                               # 0x6
	.long	65                              # 0x41
	.long	41                              # 0x29
	.long	59                              # 0x3b
	.long	22                              # 0x16
	.long	83                              # 0x53
	.long	92                              # 0x5c
	.long	38                              # 0x26
	.long	34                              # 0x22
	.long	96                              # 0x60
	.long	87                              # 0x57
	.long	96                              # 0x60
	.long	44                              # 0x2c
	.long	60                              # 0x3c
	.long	62                              # 0x3e
	.long	87                              # 0x57
	.long	47                              # 0x2f
	.long	78                              # 0x4e
	.long	41                              # 0x29
	.long	18                              # 0x12
	.long	26                              # 0x1a
	.long	54                              # 0x36
	.long	65                              # 0x41
	.long	46                              # 0x2e
	.long	25                              # 0x19
	.long	5                               # 0x5
	.long	81                              # 0x51
	.long	17                              # 0x11
	.long	48                              # 0x30
	.long	4                               # 0x4
	.long	13                              # 0xd
	.long	17                              # 0x11
	.long	75                              # 0x4b
	.long	58                              # 0x3a
	.long	52                              # 0x34
	.long	1                               # 0x1
	.long	48                              # 0x30
	.long	16                              # 0x10
	.long	89                              # 0x59
	.long	14                              # 0xe
	.long	46                              # 0x2e
	.long	83                              # 0x53
	.long	81                              # 0x51
	.long	15                              # 0xf
	.long	44                              # 0x2c
	.long	92                              # 0x5c
	.long	69                              # 0x45
	.long	77                              # 0x4d
	.long	45                              # 0x2d
	.long	4                               # 0x4
	.long	83                              # 0x53
	.long	85                              # 0x55
	.long	46                              # 0x2e
	.long	27                              # 0x1b
	.long	62                              # 0x3e
	.long	65                              # 0x41
	.long	7                               # 0x7
	.long	67                              # 0x43
	.long	25                              # 0x19
	.long	50                              # 0x32
	.long	33                              # 0x21
	.long	84                              # 0x54
	.long	69                              # 0x45
	.long	68                              # 0x44
	.long	28                              # 0x1c
	.long	34                              # 0x22
	.long	59                              # 0x3b
	.long	93                              # 0x5d
	.long	98                              # 0x62
	.long	73                              # 0x49
	.long	43                              # 0x2b
	.long	47                              # 0x2f
	.long	7                               # 0x7
	.long	74                              # 0x4a
	.long	44                              # 0x2c
	.long	46                              # 0x2e
	.long	48                              # 0x30
	.long	15                              # 0xf
	.long	17                              # 0x11
	.long	22                              # 0x16
	.long	76                              # 0x4c
	.long	2                               # 0x2
	.long	18                              # 0x12
	.long	63                              # 0x3f
	.long	49                              # 0x31
	.long	40                              # 0x28
	.long	88                              # 0x58
	.long	8                               # 0x8
	.long	99                              # 0x63
	.long	92                              # 0x5c
	.long	38                              # 0x26
	.long	23                              # 0x17
	.long	5                               # 0x5
	.long	90                              # 0x5a
	.long	98                              # 0x62
	.long	70                              # 0x46
	.long	51                              # 0x33
	.long	42                              # 0x2a
	.long	45                              # 0x2d
	.long	86                              # 0x56
	.long	2                               # 0x2
	.long	60                              # 0x3c
	.long	40                              # 0x28
	.long	45                              # 0x2d
	.long	7                               # 0x7
	.long	1                               # 0x1
	.long	63                              # 0x3f
	.long	70                              # 0x46
	.long	77                              # 0x4d
	.long	3                               # 0x3
	.long	27                              # 0x1b
	.long	67                              # 0x43
	.long	39                              # 0x27
	.long	97                              # 0x61
	.long	84                              # 0x54
	.long	52                              # 0x34
	.long	53                              # 0x35
	.long	55                              # 0x37
	.long	37                              # 0x25
	.long	47                              # 0x2f
	.long	45                              # 0x2d
	.long	65                              # 0x41
	.long	0                               # 0x0
	.long	62                              # 0x3e
	.long	83                              # 0x53
	.long	85                              # 0x55
	.long	12                              # 0xc
	.long	25                              # 0x19
	.long	85                              # 0x55
	.long	19                              # 0x13
	.long	68                              # 0x44
	.long	89                              # 0x59
	.long	86                              # 0x56
	.long	51                              # 0x33
	.long	20                              # 0x14
	.long	5                               # 0x5
	.long	52                              # 0x34
	.long	41                              # 0x29
	.long	13                              # 0xd
	.long	92                              # 0x5c
	.long	23                              # 0x17
	.long	33                              # 0x21
	.long	4                               # 0x4
	.long	43                              # 0x2b
	.long	40                              # 0x28
	.long	46                              # 0x2e
	.long	46                              # 0x2e
	.long	97                              # 0x61
	.long	57                              # 0x39
	.long	87                              # 0x57
	.long	18                              # 0x12
	.long	40                              # 0x28
	.long	82                              # 0x52
	.long	40                              # 0x28
	.long	48                              # 0x30
	.long	94                              # 0x5e
	.long	3                               # 0x3
	.long	44                              # 0x2c
	.long	82                              # 0x52
	.long	6                               # 0x6
	.long	7                               # 0x7
	.long	14                              # 0xe
	.long	6                               # 0x6
	.long	25                              # 0x19
	.long	15                              # 0xf
	.long	26                              # 0x1a
	.long	45                              # 0x2d
	.long	32                              # 0x20
	.long	88                              # 0x58
	.long	43                              # 0x2b
	.long	53                              # 0x35
	.long	88                              # 0x58
	.long	86                              # 0x56
	.long	42                              # 0x2a
	.long	12                              # 0xc
	.long	38                              # 0x26
	.long	21                              # 0x15
	.long	50                              # 0x32
	.long	24                              # 0x18
	.long	50                              # 0x32
	.long	35                              # 0x23
	.long	68                              # 0x44
	.long	98                              # 0x62
	.long	41                              # 0x29
	.long	99                              # 0x63
	.long	52                              # 0x34
	.long	4                               # 0x4
	.long	82                              # 0x52
	.long	72                              # 0x48
	.long	83                              # 0x53
	.long	14                              # 0xe
	.long	26                              # 0x1a
	.long	92                              # 0x5c
	.long	43                              # 0x2b
	.long	20                              # 0x14
	.long	68                              # 0x44
	.long	1                               # 0x1
	.long	42                              # 0x2a
	.long	67                              # 0x43
	.long	1                               # 0x1
	.long	87                              # 0x57
	.long	34                              # 0x22
	.long	78                              # 0x4e
	.long	16                              # 0x10
	.long	95                              # 0x5f
	.long	42                              # 0x2a
	.long	42                              # 0x2a
	.long	0                               # 0x0
	.long	75                              # 0x4b
	.long	53                              # 0x35
	.long	30                              # 0x1e
	.long	78                              # 0x4e
	.long	19                              # 0x13
	.long	10                              # 0xa
	.long	68                              # 0x44
	.long	55                              # 0x37
	.long	96                              # 0x60
	.long	55                              # 0x37
	.long	0                               # 0x0
	.long	2                               # 0x2
	.long	79                              # 0x4f
	.long	73                              # 0x49
	.long	60                              # 0x3c
	.long	93                              # 0x5d
	.long	59                              # 0x3b
	.long	52                              # 0x34
	.long	51                              # 0x33
	.long	72                              # 0x48
	.long	29                              # 0x1d
	.long	78                              # 0x4e
	.long	2                               # 0x2
	.long	71                              # 0x47
	.long	29                              # 0x1d
	.long	49                              # 0x31
	.long	70                              # 0x46
	.long	64                              # 0x40
	.long	84                              # 0x54
	.long	43                              # 0x2b
	.long	86                              # 0x56
	.long	61                              # 0x3d
	.long	71                              # 0x47
	.long	13                              # 0xd
	.long	11                              # 0xb
	.long	8                               # 0x8
	.long	39                              # 0x27
	.long	74                              # 0x4a
	.long	75                              # 0x4b
	.long	95                              # 0x5f
	.long	39                              # 0x27
	.long	97                              # 0x61
	.long	43                              # 0x2b
	.long	55                              # 0x37
	.long	86                              # 0x56
	.long	32                              # 0x20
	.long	60                              # 0x3c
	.long	69                              # 0x45
	.long	98                              # 0x62
	.long	9                               # 0x9
	.long	90                              # 0x5a
	.long	86                              # 0x56
	.long	40                              # 0x28
	.long	19                              # 0x13
	.long	0                               # 0x0
	.long	10                              # 0xa
	.long	8                               # 0x8
	.long	74                              # 0x4a
	.long	86                              # 0x56
	.long	74                              # 0x4a
	.long	23                              # 0x17
	.long	95                              # 0x5f
	.long	58                              # 0x3a
	.long	24                              # 0x18
	.long	37                              # 0x25
	.long	44                              # 0x2c
	.long	24                              # 0x18
	.long	48                              # 0x30
	.long	73                              # 0x49
	.long	37                              # 0x25
	.long	87                              # 0x57
	.long	63                              # 0x3f
	.long	22                              # 0x16
	.long	28                              # 0x1c
	.long	10                              # 0xa
	.long	17                              # 0x11
	.long	70                              # 0x46
	.long	91                              # 0x5b
	.long	47                              # 0x2f
	.long	21                              # 0x15
	.long	60                              # 0x3c
	.long	21                              # 0x15
	.long	2                               # 0x2
	.long	24                              # 0x18
	.long	73                              # 0x49
	.long	48                              # 0x30
	.long	55                              # 0x37
	.long	68                              # 0x44
	.long	18                              # 0x12
	.long	39                              # 0x27
	.long	47                              # 0x2f
	.long	51                              # 0x33
	.long	10                              # 0xa
	.long	41                              # 0x29
	.long	39                              # 0x27
	.long	80                              # 0x50
	.long	28                              # 0x1c
	.long	76                              # 0x4c
	.long	30                              # 0x1e
	.long	1                               # 0x1
	.long	32                              # 0x20
	.long	24                              # 0x18
	.long	1                               # 0x1
	.long	22                              # 0x16
	.long	6                               # 0x6
	.long	91                              # 0x5b
	.long	91                              # 0x5b
	.long	3                               # 0x3
	.long	42                              # 0x2a
	.long	35                              # 0x23
	.long	48                              # 0x30
	.long	11                              # 0xb
	.long	29                              # 0x1d
	.long	73                              # 0x49
	.long	71                              # 0x47
	.long	39                              # 0x27
	.long	6                               # 0x6
	.long	96                              # 0x60
	.long	62                              # 0x3e
	.long	50                              # 0x32
	.long	49                              # 0x31
	.long	41                              # 0x29
	.long	45                              # 0x2d
	.long	67                              # 0x43
	.long	18                              # 0x12
	.long	40                              # 0x28
	.long	38                              # 0x26
	.long	33                              # 0x21
	.long	93                              # 0x5d
	.long	59                              # 0x3b
	.long	58                              # 0x3a
	.long	53                              # 0x35
	.long	62                              # 0x3e
	.long	17                              # 0x11
	.long	23                              # 0x17
	.long	48                              # 0x30
	.long	66                              # 0x42
	.long	59                              # 0x3b
	.long	42                              # 0x2a
	.long	96                              # 0x60
	.long	56                              # 0x38
	.long	69                              # 0x45
	.long	7                               # 0x7
	.long	66                              # 0x42
	.long	95                              # 0x5f
	.long	26                              # 0x1a
	.long	56                              # 0x38
	.long	33                              # 0x21
	.long	81                              # 0x51
	.long	11                              # 0xb
	.long	7                               # 0x7
	.long	42                              # 0x2a
	.long	69                              # 0x45
	.long	69                              # 0x45
	.long	25                              # 0x19
	.long	67                              # 0x43
	.long	23                              # 0x17
	.long	36                              # 0x24
	.long	11                              # 0xb
	.long	95                              # 0x5f
	.long	35                              # 0x23
	.long	88                              # 0x58
	.long	96                              # 0x60
	.long	71                              # 0x47
	.long	73                              # 0x49
	.long	54                              # 0x36
	.long	79                              # 0x4f
	.long	34                              # 0x22
	.long	7                               # 0x7
	.long	32                              # 0x20
	.long	96                              # 0x60
	.long	97                              # 0x61
	.long	12                              # 0xc
	.long	86                              # 0x56
	.long	19                              # 0x13
	.long	70                              # 0x46
	.long	45                              # 0x2d
	.long	31                              # 0x1f
	.long	53                              # 0x35
	.long	56                              # 0x38
	.long	75                              # 0x4b
	.long	87                              # 0x57
	.long	95                              # 0x5f
	.long	34                              # 0x22
	.long	26                              # 0x1a
	.long	54                              # 0x36
	.long	61                              # 0x3d
	.long	4                               # 0x4
	.long	50                              # 0x32
	.long	31                              # 0x1f
	.long	33                              # 0x21
	.long	8                               # 0x8
	.long	71                              # 0x47
	.long	91                              # 0x5b
	.long	65                              # 0x41
	.long	61                              # 0x3d
	.long	40                              # 0x28
	.long	14                              # 0xe
	.long	60                              # 0x3c
	.long	57                              # 0x39
	.long	39                              # 0x27
	.long	7                               # 0x7
	.long	82                              # 0x52
	.long	87                              # 0x57
	.long	65                              # 0x41
	.long	75                              # 0x4b
	.long	72                              # 0x48
	.long	84                              # 0x54
	.long	8                               # 0x8
	.long	73                              # 0x49
	.long	7                               # 0x7
	.long	24                              # 0x18
	.long	86                              # 0x56
	.long	11                              # 0xb
	.long	15                              # 0xf
	.long	80                              # 0x50
	.long	34                              # 0x22
	.long	81                              # 0x51
	.long	31                              # 0x1f
	.long	36                              # 0x24
	.long	82                              # 0x52
	.long	93                              # 0x5d
	.long	34                              # 0x22
	.long	50                              # 0x32
	.long	40                              # 0x28
	.long	51                              # 0x33
	.long	73                              # 0x49
	.long	55                              # 0x37
	.long	83                              # 0x53
	.long	86                              # 0x56
	.long	85                              # 0x55
	.long	32                              # 0x20
	.long	21                              # 0x15
	.long	53                              # 0x35
	.long	70                              # 0x46
	.long	1                               # 0x1
	.long	31                              # 0x1f
	.long	20                              # 0x14
	.long	95                              # 0x5f
	.long	23                              # 0x17
	.long	91                              # 0x5b
	.long	61                              # 0x3d
	.long	32                              # 0x20
	.long	25                              # 0x19
	.long	80                              # 0x50
	.long	67                              # 0x43
	.long	74                              # 0x4a
	.long	28                              # 0x1c
	.long	72                              # 0x48
	.long	67                              # 0x43
	.long	96                              # 0x60
	.long	21                              # 0x15
	.long	25                              # 0x19
	.long	37                              # 0x25
	.long	35                              # 0x23
	.long	49                              # 0x31
	.long	48                              # 0x30
	.long	64                              # 0x40
	.long	79                              # 0x4f
	.long	5                               # 0x5
	.long	2                               # 0x2
	.long	83                              # 0x53
	.long	73                              # 0x49
	.long	56                              # 0x38
	.long	36                              # 0x24
	.long	86                              # 0x56
	.long	36                              # 0x24
	.long	9                               # 0x9
	.long	1                               # 0x1
	.long	69                              # 0x45
	.long	17                              # 0x11
	.long	53                              # 0x35
	.long	96                              # 0x60
	.long	59                              # 0x3b
	.long	4                               # 0x4
	.long	53                              # 0x35
	.long	99                              # 0x63
	.long	69                              # 0x45
	.long	56                              # 0x38
	.long	49                              # 0x31
	.long	53                              # 0x35
	.long	59                              # 0x3b
	.long	43                              # 0x2b
	.long	19                              # 0x13
	.long	72                              # 0x48
	.long	93                              # 0x5d
	.long	47                              # 0x2f
	.long	27                              # 0x1b
	.long	5                               # 0x5
	.long	48                              # 0x30
	.long	80                              # 0x50
	.long	4                               # 0x4
	.long	98                              # 0x62
	.long	32                              # 0x20
	.long	8                               # 0x8
	.long	79                              # 0x4f
	.long	41                              # 0x29
	.long	53                              # 0x35
	.long	88                              # 0x58
	.long	38                              # 0x26
	.long	76                              # 0x4c
	.long	57                              # 0x39
	.long	55                              # 0x37
	.long	60                              # 0x3c
	.long	16                              # 0x10
	.long	16                              # 0x10
	.long	36                              # 0x24
	.long	51                              # 0x33
	.long	17                              # 0x11
	.long	63                              # 0x3f
	.long	44                              # 0x2c
	.long	54                              # 0x36
	.long	75                              # 0x4b
	.long	80                              # 0x50
	.long	28                              # 0x1c
	.long	98                              # 0x62
	.long	9                               # 0x9
	.long	42                              # 0x2a
	.long	85                              # 0x55
	.long	25                              # 0x19
	.long	23                              # 0x17
	.long	20                              # 0x14
	.long	43                              # 0x2b
	.long	42                              # 0x2a
	.long	92                              # 0x5c
	.long	36                              # 0x24
	.long	76                              # 0x4c
	.long	49                              # 0x31
	.long	7                               # 0x7
	.long	1                               # 0x1
	.long	40                              # 0x28
	.long	83                              # 0x53
	.long	72                              # 0x48
	.long	83                              # 0x53
	.long	65                              # 0x41
	.long	80                              # 0x50
	.long	70                              # 0x46
	.long	36                              # 0x24
	.long	18                              # 0x12
	.long	91                              # 0x5b
	.long	95                              # 0x5f
	.long	31                              # 0x1f
	.long	41                              # 0x29
	.long	1                               # 0x1
	.long	55                              # 0x37
	.long	73                              # 0x49
	.long	54                              # 0x36
	.long	79                              # 0x4f
	.long	71                              # 0x47
	.long	69                              # 0x45
	.long	8                               # 0x8
	.long	5                               # 0x5
	.long	72                              # 0x48
	.long	70                              # 0x46
	.long	83                              # 0x53
	.long	70                              # 0x46
	.long	83                              # 0x53
	.long	28                              # 0x1c
	.long	81                              # 0x51
	.long	30                              # 0x1e
	.long	81                              # 0x51
	.long	51                              # 0x33
	.long	84                              # 0x54
	.long	69                              # 0x45
	.long	11                              # 0xb
	.long	8                               # 0x8
	.long	10                              # 0xa
	.long	75                              # 0x4b
	.long	23                              # 0x17
	.long	90                              # 0x5a
	.long	72                              # 0x48
	.long	13                              # 0xd
	.long	25                              # 0x19
	.long	75                              # 0x4b
	.long	84                              # 0x54
	.long	58                              # 0x3a
	.long	10                              # 0xa
	.long	49                              # 0x31
	.long	16                              # 0x10
	.long	12                              # 0xc
	.long	12                              # 0xc
	.long	33                              # 0x21
	.long	70                              # 0x46
	.long	34                              # 0x22
	.long	77                              # 0x4d
	.long	18                              # 0x12
	.long	97                              # 0x61
	.long	27                              # 0x1b
	.long	29                              # 0x1d
	.long	68                              # 0x44
	.long	82                              # 0x52
	.long	92                              # 0x5c
	.long	9                               # 0x9
	.long	34                              # 0x22
	.long	57                              # 0x39
	.long	13                              # 0xd
	.long	85                              # 0x55
	.long	98                              # 0x62
	.long	17                              # 0x11
	.long	46                              # 0x2e
	.long	76                              # 0x4c
	.long	24                              # 0x18
	.long	21                              # 0x15
	.long	62                              # 0x3e
	.long	76                              # 0x4c
	.long	64                              # 0x40
	.long	54                              # 0x36
	.long	81                              # 0x51
	.long	69                              # 0x45
	.long	42                              # 0x2a
	.long	83                              # 0x53
	.long	85                              # 0x55
	.long	38                              # 0x26
	.long	69                              # 0x45
	.long	34                              # 0x22
	.long	91                              # 0x5b
	.long	45                              # 0x2d
	.long	52                              # 0x34
	.long	92                              # 0x5c
	.long	63                              # 0x3f
	.long	30                              # 0x1e
	.long	93                              # 0x5d
	.long	81                              # 0x51
	.long	67                              # 0x43
	.long	60                              # 0x3c
	.long	61                              # 0x3d
	.long	11                              # 0xb
	.long	8                               # 0x8
	.long	87                              # 0x57
	.long	5                               # 0x5
	.long	43                              # 0x2b
	.long	52                              # 0x34
	.long	10                              # 0xa
	.long	58                              # 0x3a
	.long	23                              # 0x17
	.long	60                              # 0x3c
	.long	62                              # 0x3e
	.long	33                              # 0x21
	.long	32                              # 0x20
	.long	47                              # 0x2f
	.long	59                              # 0x3b
	.long	10                              # 0xa
	.long	81                              # 0x51
	.long	15                              # 0xf
	.long	82                              # 0x52
	.long	95                              # 0x5f
	.long	9                               # 0x9
	.long	96                              # 0x60
	.long	43                              # 0x2b
	.long	77                              # 0x4d
	.long	40                              # 0x28
	.long	70                              # 0x46
	.long	18                              # 0x12
	.long	38                              # 0x26
	.long	22                              # 0x16
	.long	38                              # 0x26
	.long	25                              # 0x19
	.long	27                              # 0x1b
	.long	33                              # 0x21
	.long	98                              # 0x62
	.long	82                              # 0x52
	.long	74                              # 0x4a
	.long	85                              # 0x55
	.long	41                              # 0x29
	.long	72                              # 0x48
	.long	96                              # 0x60
	.long	29                              # 0x1d
	.long	26                              # 0x1a
	.long	70                              # 0x46
	.long	80                              # 0x50
	.long	31                              # 0x1f
	.long	55                              # 0x37
	.long	55                              # 0x37
	.long	15                              # 0xf
	.long	5                               # 0x5
	.long	11                              # 0xb
	.long	82                              # 0x52
	.long	13                              # 0xd
	.long	15                              # 0xf
	.long	7                               # 0x7
	.long	56                              # 0x38
	.long	19                              # 0x13
	.long	57                              # 0x39
	.long	46                              # 0x2e
	.long	55                              # 0x37
	.long	43                              # 0x2b
	.long	14                              # 0xe
	.long	6                               # 0x6
	.long	45                              # 0x2d
	.long	5                               # 0x5
	.long	50                              # 0x32
	.long	4                               # 0x4
	.long	93                              # 0x5d
	.long	76                              # 0x4c
	.long	89                              # 0x59
	.long	91                              # 0x5b
	.long	2                               # 0x2
	.long	86                              # 0x56
	.long	11                              # 0xb
	.long	86                              # 0x56
	.long	2                               # 0x2
	.long	42                              # 0x2a
	.long	22                              # 0x16
	.long	66                              # 0x42
	.long	63                              # 0x3f
	.long	20                              # 0x14
	.long	28                              # 0x1c
	.long	70                              # 0x46
	.long	47                              # 0x2f
	.long	83                              # 0x53
	.long	18                              # 0x12
	.long	49                              # 0x31
	.long	85                              # 0x55
	.long	71                              # 0x47
	.long	89                              # 0x59
	.long	74                              # 0x4a
	.long	38                              # 0x26
	.long	66                              # 0x42
	.long	46                              # 0x2e
	.long	59                              # 0x3b
	.long	28                              # 0x1c
	.long	42                              # 0x2a
	.long	63                              # 0x3f
	.long	87                              # 0x57
	.long	5                               # 0x5
	.long	11                              # 0xb
	.long	18                              # 0x12
	.long	39                              # 0x27
	.long	51                              # 0x33
	.long	45                              # 0x2d
	.long	7                               # 0x7
	.long	77                              # 0x4d
	.long	7                               # 0x7
	.long	88                              # 0x58
	.long	83                              # 0x53
	.long	84                              # 0x54
	.long	91                              # 0x5b
	.long	33                              # 0x21
	.long	76                              # 0x4c
	.long	58                              # 0x3a
	.long	5                               # 0x5
	.long	52                              # 0x34
	.long	16                              # 0x10
	.long	38                              # 0x26
	.long	17                              # 0x11
	.long	95                              # 0x5f
	.long	80                              # 0x50
	.long	17                              # 0x11
	.long	27                              # 0x1b
	.long	74                              # 0x4a
	.long	5                               # 0x5
	.long	98                              # 0x62
	.long	69                              # 0x45
	.long	54                              # 0x36
	.long	2                               # 0x2
	.long	62                              # 0x3e
	.long	59                              # 0x3b
	.long	90                              # 0x5a
	.long	37                              # 0x25
	.long	24                              # 0x18
	.long	88                              # 0x58
	.long	88                              # 0x58
	.long	67                              # 0x43
	.long	97                              # 0x61
	.long	32                              # 0x20
	.long	54                              # 0x36
	.long	90                              # 0x5a
	.long	88                              # 0x58
	.long	32                              # 0x20
	.long	22                              # 0x16
	.long	42                              # 0x2a
	.long	14                              # 0xe
	.long	75                              # 0x4b
	.long	91                              # 0x5b
	.long	76                              # 0x4c
	.long	91                              # 0x5b
	.long	65                              # 0x41
	.long	21                              # 0x15
	.long	31                              # 0x1f
	.long	89                              # 0x59
	.long	42                              # 0x2a
	.long	87                              # 0x57
	.long	84                              # 0x54
	.long	35                              # 0x23
	.long	20                              # 0x14
	.long	31                              # 0x1f
	.long	49                              # 0x31
	.long	66                              # 0x42
	.long	25                              # 0x19
	.long	68                              # 0x44
	.long	98                              # 0x62
	.long	47                              # 0x2f
	.long	1                               # 0x1
	.long	44                              # 0x2c
	.long	18                              # 0x12
	.long	78                              # 0x4e
	.long	20                              # 0x14
	.long	85                              # 0x55
	.long	9                               # 0x9
	.long	21                              # 0x15
	.long	61                              # 0x3d
	.long	95                              # 0x5f
	.long	10                              # 0xa
	.long	61                              # 0x3d
	.long	92                              # 0x5c
	.long	77                              # 0x4d
	.long	69                              # 0x45
	.long	51                              # 0x33
	.long	25                              # 0x19
	.long	44                              # 0x2c
	.long	59                              # 0x3b
	.long	36                              # 0x24
	.long	14                              # 0xe
	.long	47                              # 0x2f
	.long	74                              # 0x4a
	.long	1                               # 0x1
	.long	36                              # 0x24
	.long	64                              # 0x40
	.long	80                              # 0x50
	.long	8                               # 0x8
	.long	81                              # 0x51
	.long	93                              # 0x5d
	.long	50                              # 0x32
	.long	41                              # 0x29
	.long	77                              # 0x4d
	.long	57                              # 0x39
	.long	87                              # 0x57
	.long	91                              # 0x5b
	.long	98                              # 0x62
	.long	97                              # 0x61
	.long	54                              # 0x36
	.long	28                              # 0x1c
	.long	91                              # 0x5b
	.long	4                               # 0x4
	.long	4                               # 0x4
	.long	89                              # 0x59
	.long	85                              # 0x55
	.long	15                              # 0xf
	.long	53                              # 0x35
	.long	2                               # 0x2
	.long	77                              # 0x4d
	.long	7                               # 0x7
	.long	87                              # 0x57
	.long	29                              # 0x1d
	.long	98                              # 0x62
	.long	45                              # 0x2d
	.long	94                              # 0x5e
	.long	77                              # 0x4d
	.long	55                              # 0x37
	.long	16                              # 0x10
	.long	46                              # 0x2e
	.long	20                              # 0x14
	.long	12                              # 0xc
	.long	42                              # 0x2a
	.long	62                              # 0x3e
	.long	25                              # 0x19
	.long	5                               # 0x5
	.long	75                              # 0x4b
	.long	26                              # 0x1a
	.long	41                              # 0x29
	.long	2                               # 0x2
	.long	76                              # 0x4c
	.long	27                              # 0x1b
	.long	86                              # 0x56
	.long	27                              # 0x1b
	.long	68                              # 0x44
	.long	9                               # 0x9
	.long	19                              # 0x13
	.long	56                              # 0x38
	.long	34                              # 0x22
	.long	93                              # 0x5d
	.long	23                              # 0x17
	.long	39                              # 0x27
	.long	69                              # 0x45
	.long	90                              # 0x5a
	.long	19                              # 0x13
	.long	47                              # 0x2f
	.long	90                              # 0x5a
	.long	41                              # 0x29
	.long	74                              # 0x4a
	.long	81                              # 0x51
	.long	55                              # 0x37
	.long	74                              # 0x4a
	.long	66                              # 0x42
	.long	95                              # 0x5f
	.long	33                              # 0x21
	.long	62                              # 0x3e
	.long	1                               # 0x1
	.long	29                              # 0x1d
	.long	73                              # 0x49
	.long	82                              # 0x52
	.long	56                              # 0x38
	.long	92                              # 0x5c
	.long	96                              # 0x60
	.long	53                              # 0x35
	.long	10                              # 0xa
	.long	15                              # 0xf
	.long	14                              # 0xe
	.long	90                              # 0x5a
	.long	55                              # 0x37
	.long	36                              # 0x24
	.long	90                              # 0x5a
	.long	60                              # 0x3c
	.long	76                              # 0x4c
	.long	99                              # 0x63
	.long	36                              # 0x24
	.long	50                              # 0x32
	.long	16                              # 0x10
	.long	77                              # 0x4d
	.long	88                              # 0x58
	.long	88                              # 0x58
	.long	36                              # 0x24
	.long	53                              # 0x35
	.long	86                              # 0x56
	.long	90                              # 0x5a
	.long	99                              # 0x63
	.long	47                              # 0x2f
	.long	8                               # 0x8
	.long	2                               # 0x2
	.long	97                              # 0x61
	.long	7                               # 0x7
	.long	83                              # 0x53
	.long	9                               # 0x9
	.long	37                              # 0x25
	.long	41                              # 0x29
	.long	86                              # 0x56
	.long	14                              # 0xe
	.long	1                               # 0x1
	.long	99                              # 0x63
	.long	63                              # 0x3f
	.long	12                              # 0xc
	.size	.L__const.init.var2, 5776

	.type	.L__const.init.sbox,@object     # @__const.init.sbox
	.p2align	4
.L__const.init.sbox:
	.long	222                             # 0xde
	.long	59                              # 0x3b
	.long	254                             # 0xfe
	.long	34                              # 0x22
	.long	195                             # 0xc3
	.long	240                             # 0xf0
	.long	178                             # 0xb2
	.long	176                             # 0xb0
	.long	74                              # 0x4a
	.long	125                             # 0x7d
	.long	204                             # 0xcc
	.long	134                             # 0x86
	.long	29                              # 0x1d
	.long	55                              # 0x37
	.long	82                              # 0x52
	.long	84                              # 0x54
	.long	241                             # 0xf1
	.long	105                             # 0x69
	.long	17                              # 0x11
	.long	27                              # 0x1b
	.long	23                              # 0x17
	.long	71                              # 0x47
	.long	121                             # 0x79
	.long	63                              # 0x3f
	.long	188                             # 0xbc
	.long	22                              # 0x16
	.long	39                              # 0x27
	.long	18                              # 0x12
	.long	248                             # 0xf8
	.long	133                             # 0x85
	.long	235                             # 0xeb
	.long	148                             # 0x94
	.long	190                             # 0xbe
	.long	93                              # 0x5d
	.long	12                              # 0xc
	.long	30                              # 0x1e
	.long	67                              # 0x43
	.long	89                              # 0x59
	.long	44                              # 0x2c
	.long	56                              # 0x38
	.long	146                             # 0x92
	.long	101                             # 0x65
	.long	95                              # 0x5f
	.long	79                              # 0x4f
	.long	161                             # 0xa1
	.long	162                             # 0xa2
	.long	76                              # 0x4c
	.long	183                             # 0xb7
	.long	184                             # 0xb8
	.long	72                              # 0x48
	.long	210                             # 0xd2
	.long	2                               # 0x2
	.long	21                              # 0x15
	.long	165                             # 0xa5
	.long	28                              # 0x1c
	.long	198                             # 0xc6
	.long	0                               # 0x0
	.long	171                             # 0xab
	.long	122                             # 0x7a
	.long	139                             # 0x8b
	.long	123                             # 0x7b
	.long	144                             # 0x90
	.long	4                               # 0x4
	.long	247                             # 0xf7
	.long	253                             # 0xfd
	.long	112                             # 0x70
	.long	157                             # 0x9d
	.long	185                             # 0xb9
	.long	189                             # 0xbd
	.long	13                              # 0xd
	.long	116                             # 0x74
	.long	110                             # 0x6e
	.long	64                              # 0x40
	.long	96                              # 0x60
	.long	10                              # 0xa
	.long	24                              # 0x18
	.long	154                             # 0x9a
	.long	35                              # 0x23
	.long	25                              # 0x19
	.long	19                              # 0x13
	.long	60                              # 0x3c
	.long	73                              # 0x49
	.long	186                             # 0xba
	.long	11                              # 0xb
	.long	138                             # 0x8a
	.long	136                             # 0x88
	.long	26                              # 0x1a
	.long	250                             # 0xfa
	.long	46                              # 0x2e
	.long	124                             # 0x7c
	.long	129                             # 0x81
	.long	9                               # 0x9
	.long	62                              # 0x3e
	.long	174                             # 0xae
	.long	187                             # 0xbb
	.long	111                             # 0x6f
	.long	212                             # 0xd4
	.long	207                             # 0xcf
	.long	209                             # 0xd1
	.long	251                             # 0xfb
	.long	113                             # 0x71
	.long	226                             # 0xe2
	.long	182                             # 0xb6
	.long	14                              # 0xe
	.long	92                              # 0x5c
	.long	131                             # 0x83
	.long	3                               # 0x3
	.long	119                             # 0x77
	.long	43                              # 0x2b
	.long	211                             # 0xd3
	.long	68                              # 0x44
	.long	246                             # 0xf6
	.long	81                              # 0x51
	.long	7                               # 0x7
	.long	169                             # 0xa9
	.long	228                             # 0xe4
	.long	143                             # 0x8f
	.long	54                              # 0x36
	.long	150                             # 0x96
	.long	158                             # 0x9e
	.long	217                             # 0xd9
	.long	108                             # 0x6c
	.long	126                             # 0x7e
	.long	160                             # 0xa0
	.long	49                              # 0x31
	.long	98                              # 0x62
	.long	197                             # 0xc5
	.long	107                             # 0x6b
	.long	75                              # 0x4b
	.long	163                             # 0xa3
	.long	173                             # 0xad
	.long	147                             # 0x93
	.long	128                             # 0x80
	.long	51                              # 0x33
	.long	172                             # 0xac
	.long	15                              # 0xf
	.long	200                             # 0xc8
	.long	229                             # 0xe5
	.long	175                             # 0xaf
	.long	239                             # 0xef
	.long	97                              # 0x61
	.long	115                             # 0x73
	.long	83                              # 0x53
	.long	216                             # 0xd8
	.long	114                             # 0x72
	.long	199                             # 0xc7
	.long	244                             # 0xf4
	.long	149                             # 0x95
	.long	57                              # 0x39
	.long	249                             # 0xf9
	.long	236                             # 0xec
	.long	203                             # 0xcb
	.long	53                              # 0x35
	.long	213                             # 0xd5
	.long	70                              # 0x46
	.long	230                             # 0xe6
	.long	94                              # 0x5e
	.long	5                               # 0x5
	.long	52                              # 0x34
	.long	91                              # 0x5b
	.long	164                             # 0xa4
	.long	1                               # 0x1
	.long	151                             # 0x97
	.long	141                             # 0x8d
	.long	245                             # 0xf5
	.long	48                              # 0x30
	.long	140                             # 0x8c
	.long	214                             # 0xd6
	.long	132                             # 0x84
	.long	36                              # 0x24
	.long	218                             # 0xda
	.long	127                             # 0x7f
	.long	191                             # 0xbf
	.long	42                              # 0x2a
	.long	41                              # 0x29
	.long	66                              # 0x42
	.long	61                              # 0x3d
	.long	196                             # 0xc4
	.long	104                             # 0x68
	.long	80                              # 0x50
	.long	20                              # 0x14
	.long	86                              # 0x56
	.long	219                             # 0xdb
	.long	88                              # 0x58
	.long	166                             # 0xa6
	.long	179                             # 0xb3
	.long	37                              # 0x25
	.long	252                             # 0xfc
	.long	215                             # 0xd7
	.long	78                              # 0x4e
	.long	33                              # 0x21
	.long	170                             # 0xaa
	.long	233                             # 0xe9
	.long	180                             # 0xb4
	.long	194                             # 0xc2
	.long	32                              # 0x20
	.long	238                             # 0xee
	.long	45                              # 0x2d
	.long	69                              # 0x45
	.long	77                              # 0x4d
	.long	50                              # 0x32
	.long	224                             # 0xe0
	.long	103                             # 0x67
	.long	193                             # 0xc1
	.long	243                             # 0xf3
	.long	47                              # 0x2f
	.long	130                             # 0x82
	.long	159                             # 0x9f
	.long	201                             # 0xc9
	.long	109                             # 0x6d
	.long	118                             # 0x76
	.long	65                              # 0x41
	.long	177                             # 0xb1
	.long	221                             # 0xdd
	.long	6                               # 0x6
	.long	120                             # 0x78
	.long	8                               # 0x8
	.long	232                             # 0xe8
	.long	106                             # 0x6a
	.long	223                             # 0xdf
	.long	31                              # 0x1f
	.long	85                              # 0x55
	.long	225                             # 0xe1
	.long	205                             # 0xcd
	.long	168                             # 0xa8
	.long	117                             # 0x75
	.long	242                             # 0xf2
	.long	155                             # 0x9b
	.long	206                             # 0xce
	.long	237                             # 0xed
	.long	192                             # 0xc0
	.long	227                             # 0xe3
	.long	142                             # 0x8e
	.long	40                              # 0x28
	.long	220                             # 0xdc
	.long	87                              # 0x57
	.long	234                             # 0xea
	.long	58                              # 0x3a
	.long	202                             # 0xca
	.long	100                             # 0x64
	.long	99                              # 0x63
	.long	208                             # 0xd0
	.long	90                              # 0x5a
	.long	167                             # 0xa7
	.long	231                             # 0xe7
	.long	152                             # 0x98
	.long	145                             # 0x91
	.long	156                             # 0x9c
	.long	38                              # 0x26
	.long	255                             # 0xff
	.long	16                              # 0x10
	.long	137                             # 0x89
	.long	102                             # 0x66
	.long	181                             # 0xb5
	.long	153                             # 0x99
	.long	135                             # 0x87
	.size	.L__const.init.sbox, 1024

	.type	.L__const.init.var1,@object     # @__const.init.var1
	.p2align	4
.L__const.init.var1:
	.long	33145                           # 0x8179
	.long	34686                           # 0x877e
	.long	30905                           # 0x78b9
	.long	34909                           # 0x885d
	.long	31950                           # 0x7cce
	.long	37332                           # 0x91d4
	.long	33139                           # 0x8173
	.long	31764                           # 0x7c14
	.long	38082                           # 0x94c2
	.long	33686                           # 0x8396
	.long	40370                           # 0x9db2
	.long	39120                           # 0x98d0
	.long	30072                           # 0x7578
	.long	33304                           # 0x8218
	.long	34077                           # 0x851d
	.long	35350                           # 0x8a16
	.long	32017                           # 0x7d11
	.long	33007                           # 0x80ef
	.long	41814                           # 0xa356
	.long	30235                           # 0x761b
	.long	35717                           # 0x8b85
	.long	37183                           # 0x913f
	.long	34267                           # 0x85db
	.long	32465                           # 0x7ed1
	.long	32446                           # 0x7ebe
	.long	31242                           # 0x7a0a
	.long	31575                           # 0x7b57
	.long	31967                           # 0x7cdf
	.long	37445                           # 0x9245
	.long	41662                           # 0xa2be
	.long	34591                           # 0x871f
	.long	30458                           # 0x76fa
	.long	36938                           # 0x904a
	.long	33172                           # 0x8194
	.long	38446                           # 0x962e
	.long	36083                           # 0x8cf3
	.long	37176                           # 0x9138
	.long	27046                           # 0x69a6
	.size	.L__const.init.var1, 152

	.type	.L__const.init.var6,@object     # @__const.init.var6
	.p2align	4
.L__const.init.var6:
	.long	117                             # 0x75
	.long	234                             # 0xea
	.long	139                             # 0x8b
	.long	126                             # 0x7e
	.long	231                             # 0xe7
	.long	161                             # 0xa1
	.long	177                             # 0xb1
	.long	160                             # 0xa0
	.long	169                             # 0xa9
	.long	235                             # 0xeb
	.long	176                             # 0xb0
	.long	243                             # 0xf3
	.long	129                             # 0x81
	.long	225                             # 0xe1
	.long	155                             # 0x9b
	.long	216                             # 0xd8
	.long	99                              # 0x63
	.long	168                             # 0xa8
	.long	208                             # 0xd0
	.long	211                             # 0xd3
	.long	147                             # 0x93
	.long	195                             # 0xc3
	.long	157                             # 0x9d
	.long	122                             # 0x7a
	.long	171                             # 0xab
	.long	201                             # 0xc9
	.long	163                             # 0xa3
	.long	249                             # 0xf9
	.long	140                             # 0x8c
	.long	176                             # 0xb0
	.long	174                             # 0xae
	.long	245                             # 0xf5
	.long	146                             # 0x92
	.long	208                             # 0xd0
	.long	224                             # 0xe0
	.long	227                             # 0xe3
	.long	184                             # 0xb8
	.long	205                             # 0xcd
	.size	.L__const.init.var6, 152

	.type	.L.str.2,@object                # @.str.2
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str.2:
	.asciz	"Enter your input: "
	.size	.L.str.2, 19

	.type	.L.str.3,@object                # @.str.3
.L.str.3:
	.asciz	"%s\n"
	.size	.L.str.3, 4

	.type	.L.str.4,@object                # @.str.4
.L.str.4:
	.asciz	"Goodbye and see you next time!!! XD\n"
	.size	.L.str.4, 37

	.section	".note.GNU-stack","",@progbits
